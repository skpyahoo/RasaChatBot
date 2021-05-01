from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted
import zomatopy
import json
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from bs4 import BeautifulSoup
import re
import requests
import pprint
from flask_mail import Mail, Message
from flask import Flask
from flask_cors import CORS, cross_origin
from gevent.pywsgi import WSGIServer
from Soundex import get_soundex

import urllib3
urllib3.disable_warnings()

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		
		config={"user_key":"78776f52922c6d8a2c4a5e5e934f724a"}
		zomato = zomatopy.initialize_app(config)
		
		cuisine = tracker.get_slot('cuisine')
		cuisines=['chinese','mexican','italian','american','south indian','north indian']
		soundex_dct={get_soundex(value):value for value in cuisines}
		if get_soundex(cuisine) in soundex_dct.keys():
		
			cuisine=soundex_dct[get_soundex(cuisine)]
		
		loc = tracker.get_slot('location')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		
		price=tracker.get_slot('price')
		temp_dict={'1':[0,300],'2':[300,700],'3':[700]}
		
		try:
			lat=d1["location_suggestions"][0]["latitude"]
			lon=d1["location_suggestions"][0]["longitude"]
			
			cuisines_dict={'mexican':73,'chinese':25,'american':1,'italian':55,'north indian':50,'south indian':85}
			
			lst=[]
			for r in range(0,100,20):
				results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), start=r)
				d = json.loads(results)
				for restaurant in d['restaurants']:
					lst.append((restaurant['restaurant']['name'],restaurant['restaurant']['location']['address'],float(restaurant['restaurant']['average_cost_for_two']),float(restaurant['restaurant']['user_rating']['aggregate_rating'])))
			
			temp=['max','maximum','less','lesser','not more','<']
			if len(price)==1:
				price.append(0)
			
			for i in range(len(price)):
				if isinstance(price[i],str):
					if price[i].lower() in temp:
						price[i]=0
			temp=['min','minimum','more','higher','greater','>']
			
			for value in price:
				if isinstance(value,str):
					if value.lower() in temp:
						price.remove(value)
			
			price=list(map(float,price))
			price=sorted(price)
			
			lst1=sorted(lst,key=lambda x:x[3],reverse=True)
			if len(price)==1:
				final_lst=list(filter(lambda x:x[2]>=price[0],lst1))[:10]
			else:
				final_lst=list(filter(lambda x:x[2]>=price[0] and x[2]<=price[1],lst1))[:10]
				
			response=""
			if len(final_lst) == 0:
				response= "no results"
			else:
				response="Showing you top rated restaurants: "
				for restaurant in final_lst[:5]:
					response=response+ restaurant[0]+ " in "+ restaurant[1]+" has been rated "+str(restaurant[3])+ ". And the average price for two people here is Rs "+ str(restaurant[2])+"."+"\n"
				restaurant_final_list=final_lst[:10]
				
				file=open("restaurant.txt","w+",encoding='utf-8')
				counter=1
				#dispatcher.utter_message("Writing in a file")
				for restaurant in restaurant_final_list:
					file.write("{}. Restaurant Name: {}\n Restaurant locality address: {}\n Average budget for two people: {}\n Zomato user rating: {}\n\n".format(counter,restaurant[0],restaurant[1],restaurant[2],restaurant[3]))
					counter+=1
				file.close()
		except:
			response="no results"
		dispatcher.utter_message(response)
		
		return [SlotSet('cuisine',cuisine),SlotSet('noresults',response=="no results")]
		
class ActionGetCity(Action):
	def name(self):
		return 'action_city'
	
	def run(self, dispatcher, tracker, domain):
		
		url="https://en.wikipedia.org/wiki/Classification_of_Indian_cities"
		r = requests.get(url,verify=False)
		soup = BeautifulSoup(r.text, "lxml")
		#print (soup.prettify())
		match = soup.find('table',class_='wikitable').find_all('a')
		#print(match)
		tier_cities=list(map(lambda x:x.text.lower(),soup.find('table',class_='wikitable').find_all('a')))
		
		synonym_names={}
		r=requests.get('https://www.scoopwhoop.com/news/whats-in-a-name/#.45rdcz1m2',verify=False)
		containers=BeautifulSoup(r.text,'lxml').find('div',class_='article-body').find_all('h2')
		
		for container in containers:
			if re.search(r'^[0-9]{1,2}.+',container.text.strip()):
				synonym_names[container.text.strip().split()[1].lower()]=container.text.strip().split()[-1].lower()
		
		for index,value in enumerate(tier_cities):
			if value in synonym_names.keys():
				tier_cities[index]=synonym_names[value]
		
		soundex_dict_tier={get_soundex(name):name for name in tier_cities}
		soundex_dict_syn={get_soundex(key):value for key,value in synonym_names.items()}
		
		loc=tracker.get_slot('location')
		loc_soundex=get_soundex(loc)
		
		val=False
		if loc_soundex in soundex_dict_tier.keys():
			val=True
			loc=soundex_dict_tier[loc_soundex]
		if loc_soundex in soundex_dict_syn.keys() and not val:
			val=True
			loc=soundex_dict_syn[loc_soundex]
		
		return [SlotSet('location',loc),SlotSet('location_type',val)]


class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'
	
	def run(self,dispatcher,tracker,domain):
		#dispatcher.utter_message("mailcomposition start")
		body=""
		file=open('restaurant.txt','r')
		
		for line in file.readlines():
			body+=line
		file.close()
		
		to=tracker.get_slot('email')
		
		emailId="restaurant.finder2019@gmail.com"
		email_password="Restaurant@2019@1234"
		mail_from=emailId
		subject=" Top 10 Restaurant in "+tracker.get_slot("location").title()
		
		msg = MIMEMultipart()
		msg['From'] = 'Restaurant Finder'
		msg['To'] = to
		msg['Subject'] = subject
		msg.attach(MIMEText(body,'plain'))
		email_text = msg.as_string()
		try:  
			server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
			server.ehlo()
			server.login(emailId, email_password)
			server.sendmail(mail_from, to, email_text)
			server.close()
			dispatcher.utter_message(template="utter_email_Sent")
		except smtplib.SMTPException: # Didn't make an instance.
			pass
		except smtplib.socket.error:
			pass
		except:		
			dispatcher.utter_message(template="utter_email_error")
			
		
		return [SlotSet('email',to)]

class ActionResetSlots(Action):
	def name(self):
		return 'action_reset'
		
	def run(self, dispatcher, tracker, domain):
		#AllSlotsReset()
		return [AllSlotsReset()]

class ActionRestarted(Action): 	
    def name(self): 		
        return 'action_restarted' 	
    def run(self, dispatcher, tracker, domain): 
        return[Restarted()] 


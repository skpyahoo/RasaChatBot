## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_city
	- slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": ["more","300"]}
    - slot{"price":"300"}
    - action_search_restaurants
    - slot{"noresults": false}
	- utter_ask_mail_confirmation
* affirm
	- utter_ask_mail
* send_mail{"email": "skpyahoo@gmail.com"}
	- slot{"email": "skpyahoo@gmail.com"}
	- action_send_mail
* goodbye
	- utter_goodbye
	- action_reset
	- action_restarted



## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "saharanpur"}
    - slot{"location": "saharanpur"}
    - action_city
    - slot{"location": "saharanpur"}
    - slot{"location_type": false}
    - utter_noService
* goodbye
	- utter_goodbye
	- action_reset
	- action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "lucknow"}
    - slot{"location": "lucknow"}
    - action_city
    - slot{"location": "lucknow"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "1200"}
    - slot{"price": ["less", "1200"]}
    - action_search_restaurants
    - slot{"cuisine": "north indian"}
    - slot{"noresults": false}
    - utter_ask_mail_confirmation
* send_mail{"email": "sagarpahlajani@gmail.com"}
    - slot{"email": "sagarpahlajani@gmail.com"}
    - action_send_mail
    - slot{"email": "sagarpahlajani@gmail.com"}
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "raipur"}
    - slot{"location": "raipur"}
    - action_city
    - slot{"location": "raipur"}
    - slot{"location_type": true}
    - utter_ask_price
* restaurant_search{"price": "950"}
    - slot{"price": ["more", "950"]}
    - action_search_restaurants
    - slot{"cuisine": "american"}
    - slot{"noresults": false}
    - utter_ask_mail_confirmation
* send_mail{"email": "sagarpahlajani@gmail.com"}
    - slot{"email": "sagarpahlajani@gmail.com"}
    - action_send_mail
    - slot{"email": "sagarpahlajani@gmail.com"}
* affirm
    - utter_thanks
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "korea"}
    - slot{"location": "korea"}
    - action_city
    - slot{"location": "korea"}
    - slot{"location_type": false}
    - utter_noService
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - slot{"price": ["300"]}
    - action_search_restaurants
    - slot{"cuisine": "mexican"}
    - slot{"noresults": false}
    - utter_ask_mail_confirmation
* affirm
    - utter_ask_mail
* send_mail{"email": "ishamandrekar@gmail.com"}
    - slot{"email": "ishamandrekar@gmail.com"}
    - action_send_mail
    - slot{"email": "ishamandrekar@gmail.com"}
* affirm
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bijapur"}
    - slot{"location": "bijapur"}
    - action_city
    - slot{"location": "bijapur"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "100"}
    - slot{"price": ["less", "100"]}
    - action_search_restaurants
    - slot{"cuisine": "chinese"}
    - slot{"noresults": true}
    - utter_noresults
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "bombay"}
    - slot{"location": "bombay"}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "650"}
    - slot{"price": ["more", "650"]}
    - action_search_restaurants
    - slot{"cuisine": "south indian"}
    - slot{"noresults": false}
    - utter_ask_mail_confirmation
* negative
    - utter_thanks
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "tirur"}
    - slot{"location": "tirur"}
    - action_city
    - slot{"location": "tirur"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "700"}
    - slot{"price": ["300", "700"]}
    - action_search_restaurants
    - slot{"cuisine": "south indian"}
    - slot{"noresults": true}
    - utter_noresults
* restaurant_search{"price": "500"}
    - slot{"price": ["less", "500"]}
    - action_search_restaurants
    - slot{"cuisine": "south indian"}
    - slot{"noresults": true}
	- utter_noresults
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_search_restaurants
    - slot{"cuisine": "north indian"}
    - slot{"noresults": true}
    - utter_noresults
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - action_city
    - slot{"location": "agra"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "700"}
    - slot{"price": ["300", "700"]}
    - action_search_restaurants
    - slot{"cuisine": "north indian"}
    - slot{"noresults": false}
    - utter_ask_mail_confirmation
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_city
    - slot{"location": "chennai"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "700"}
    - slot{"price": ["300", "700"]}
    - action_search_restaurants
    - slot{"cuisine": "south indian"}
    - slot{"noresults": false}
    - utter_ask_mail_confirmation
* negative
    - utter_thanks
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "banda"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "banda"}
    - action_city
    - slot{"location": "bhiwandi"}
    - slot{"location_type": true}
    - utter_ask_price
* restaurant_search{"price": "700"}
    - slot{"price": ["300", "700"]}
    - action_search_restaurants
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_mail_confirmation
* send_mail{"email": "skpyahoo@gmail.com"}
    - slot{"email": "skpyahoo@gmail.com"}
    - action_send_mail
    - slot{"email": "skpyahoo@gmail.com"}
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "atarra"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "atarra"}
    - action_city
    - slot{"location": "atarra"}
    - slot{"location_type": false}
    - utter_noService
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "bombay"}
    - slot{"cuisine": "american"}
    - slot{"location": "bombay"}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - utter_ask_price
* restaurant_search{"price": "200"}
    - slot{"price": ["greater", "200"]}
    - action_search_restaurants
    - slot{"cuisine": "american"}
    - slot{"noresults": false}
    - utter_ask_mail_confirmation
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_search_restaurants
    - slot{"cuisine": "mexican"}
    - slot{"noresults": false}
    - utter_ask_mail_confirmation
* affirm
    - utter_ask_mail
* send_mail{"email": "sagarpahlajani@gmail.com"}
    - slot{"email": "sagarpahlajani@gmail.com"}
    - action_send_mail
    - slot{"email": "sagarpahlajani@gmail.com"}
* affirm
    - utter_thanks
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "411044"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "411044"}
    - action_city
    - slot{"location": "411044"}
    - slot{"location_type": false}
    - utter_noService
* restaurant_search{"location": "pune", "price": "400"}
    - slot{"location": "pune"}
    - slot{"price": ["<", "400"]}
    - action_search_restaurants
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_mail_confirmation
* send_mail{"email": "sagarpahlajani@gmail.com"}
    - slot{"email": "sagarpahlajani@gmail.com"}
    - action_send_mail
    - slot{"email": "sagarpahlajani@gmail.com"}
* affirm
    - utter_thanks
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "delhi", "price": "1500"}
    - slot{"cuisine": "italian"}
    - slot{"location": "delhi"}
    - slot{"price": ["500", "1500"]}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - action_search_restaurants
    - slot{"cuisine": "italian"}
    - slot{"noresults": false}
    - utter_ask_mail_confirmation
* send_mail{"email": "sagarpahlajani@gmail.com"}
    - slot{"email": "sagarpahlajani@gmail.com"}
    - action_send_mail
    - slot{"email": "sagarpahlajani@gmail.com"}
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "people": "5", "location": "kolkata", "price": "800"}
    - slot{"cuisine": "american"}
    - slot{"location": "kolkata"}
    - slot{"price": ["max", "800"]}
    - action_city
    - slot{"location": "kolkata"}
    - slot{"location_type": true}
    - action_search_restaurants
    - slot{"cuisine": "american"}
    - slot{"noresults": false}
    - utter_ask_mail_confirmation
* negative
    - utter_thanks
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "price": "800", "location": "atarra"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "atarra"}
    - slot{"price": ["400", "800"]}
    - action_city
    - slot{"location": "atarra"}
    - slot{"location_type": false}
    - utter_noService
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_city
    - slot{"location": "bengaluru"}
    - slot{"location_type": true}
    - action_search_restaurants
    - slot{"cuisine": "mexican"}
    - slot{"noresults": false}
    - utter_ask_mail_confirmation
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "delhi", "price": "300"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "delhi"}
    - slot{"price": ["less", "300"]}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - action_search_restaurants
    - slot{"cuisine": "north indian"}
    - slot{"noresults": false}
    - utter_ask_mail_confirmation
* restaurant_search{"price": "200"}
    - slot{"price": ["less", "200"]}
    - action_search_restaurants
    - slot{"cuisine": "north indian"}
    - slot{"noresults": false}
    - utter_ask_mail_confirmation
* negative
    - utter_thanks
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "pune", "price": "100"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "pune"}
    - slot{"price": ["less", "100"]}
    - action_city
    - slot{"location": "pune"}
    - slot{"location_type": true}
    - action_search_restaurants
    - slot{"cuisine": "mexican"}
    - slot{"noresults": true}
    - utter_noresults
* restaurant_search{"price": "500"}
    - slot{"price": ["less", "500"]}
    - action_search_restaurants
    - slot{"cuisine": "mexican"}
    - slot{"noresults": false}
    - utter_ask_mail_confirmation
* send_mail{"email": "mandhyani.tripti@gmail.com"}
    - slot{"email": "mandhyani.tripti@gmail.com"}
    - action_send_mail
    - slot{"email": "mandhyani.tripti@gmail.com"}
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_city
    - slot{"location": "bengaluru"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "700"}
    - slot{"price": ["300", "700"]}
    - action_search_restaurants
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_mail_confirmation
* send_mail{"email": "sagarpahlajani@gmail.com"}
    - slot{"email": "sagarpahlajani@gmail.com"}
    - action_send_mail
    - slot{"email": "sagarpahlajani@gmail.com"}
* send_mail{"email": "sagarpahlajani@gmail.com"}
    - slot{"email": "sagarpahlajani@gmail.com"}
    - action_send_mail
    - slot{"email": "sagarpahlajani@gmail.com"}
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_city
    - slot{"location": "bengaluru"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "800"}
    - slot{"price": ["300", "800"]}
    - action_search_restaurants
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_mail_confirmation
* send_mail{"email": "sagarpahlajani@gmail.com"}
    - slot{"email": "sagarpahlajani@gmail.com"}
    - action_send_mail
    - slot{"email": "sagarpahlajani@gmail.com"}
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_city
    - slot{"location": "mubaim"}
    - slot{"location_type": false}
    - utter_noService
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "700"}
    - slot{"price": [">", "700"]}
    - action_search_restaurants
    - slot{"cuisine": "american"}
    - slot{"noresults": false}
    - utter_ask_mail_confirmation
* affirm
    - utter_ask_mail
* send_mail{"email": "skpyahoo@gmail.com"}
    - slot{"email": "skpyahoo@gmail.com"}
    - action_send_mail
    - slot{"email": "skpyahoo@gmail.com"}
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

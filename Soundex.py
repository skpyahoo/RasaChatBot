#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def get_soundex(token):
    """Get the soundex code for the string"""
    token = token.upper()

    soundex = ""
    
    # first letter of input is always the first letter of soundex
    soundex += token[0]
    
    # create a dictionary which maps letters to respective soundex codes. Vowels and 'H', 'W' and 'Y' will be represented by '.'
    dictionary = {"BFPV": "1", "CGJKQSXZ":"2", "DT":"3", "L":"4", "MN":"5", "R":"6", "AEIOUHWY":"."}

    for char in token[1:]:
        for key in dictionary.keys():
            if char in key:
                code = dictionary[key]
                if code != soundex[-1]:
                    soundex += code

    # remove vowels and 'H', 'W' and 'Y' from soundex
    soundex = soundex.replace(".", "")
    
    # trim or pad to make soundex a 4-character code
    soundex = soundex[:4].ljust(4, "0")
        
    return soundex


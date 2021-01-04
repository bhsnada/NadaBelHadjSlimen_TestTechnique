#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime #importation de la bibliotèque datetime
def log_content(function):
    def new_function(a, b,c): 
        resultat = function(a, b,c) 
        
        print('[',datetime.now(),'][file:test.py]DEBUG [@example] variable a =',b+c)
        print('[',datetime.now(),'][file:test.py]DEBUG [@example] variable b =',a+c)
        print('[',datetime.now(),'][file:test.py]DEBUG [@example] variable c =',a+b)
        d = "hi there"
        print('[',datetime.now(),'][file:test.py]DEBUG [@example] variable d =',d)
       
        return print('[',datetime.now(),'][file:test.py]DEBUG [@example] variable result =',resultat)


    return new_function 
@log_content
def addition(a, b,c):
    a=b+c
    b=a+c
    c=a+b
  
    result = a + b + c
    return result
addition(2,3,4)


# In[ ]:





import requests
import os
from datetime import datetime 

userkey=("a6fcce494ce0c664ed5b48eaa1af926f")
locationcity=input("Enter the city name of which you would like to view the forecast.")

completeapilinkcity="https://api.openweathermap.org/data/2.5/weather?q="+locationcity+"&appid="+userkey
###DONT forget ZIP addition 
api_link=requests.get(completeapilinkcity)
api_datainfo=api_link.json() 
print (api_datainfo)


##REFINE this to where it is in a more readable format

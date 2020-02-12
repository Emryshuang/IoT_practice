import urllib
import psutil
import requests
import socket
import re

class Cloud(object):
    __api_key = ""
    __url = ""
    __dataid = ""



    def __init__(self,api_key,url,dataid):
        self.__api_key = api_key
        self.__url = "http://api.heclouds.com/devices/"+url+"/datapoints"
        self.__dataid = dataid

    def print_info(self):
        print(self.__api_key+self.__url+self.__dataid+"\n")
    
    def sent_to_iot_platform(self,datas):

        #url = "http://api.heclouds.com/devices/578657702/datapoints"
        print("before send\n")

        print(datas)
        
        params = {
            "datastreams": [
                {
                    "id":self.__dataid,
                    "datapoints":[
                        {
                            "at": "",
                            "value": datas
                        }
                    ]
                }
            ]
        }
        headers = {
            "api-key": self.__api_key,
            "Centent-type": "application/json"        
        }
    
        response = requests.post(self.__url,json=params,headers=headers)
        print("after send\n")
        return response.text
    
    
    

    

    
    

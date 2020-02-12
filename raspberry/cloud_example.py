import urllib
import psutil
import requests
import socket
import re



def get_memory_info():
    memory_info = {}
    mem =psutil.virtual_memory()
    memory_info['mem_free']=round(float(mem.total)/1000000000,3)
    memory_info['mem_total']=round(float(mem.free)/1000000000,3)
    memory_info['mem_usage_percent']=int(round(mem.percent))
    return memory_info

def get_cpu_usage_percent():
    cpu_usage_percent = psutil.cpu_percent(interval=1)
    return cpu_usage_percent

def get_intranet_ip():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def get_internet_ip():
    url = urllib.request.urlopen("http://txt.go.sohu.com/ip/soip")
    text = url.read()
    ip = re.findall(r'\d+.\d+.\d+.\d+',text.decode("UTF-8"))
    return ip[0]
         
    



def sent_to_iot_platform(memory_info):

    url = "http://api.heclouds.com/devices/578657702/datapoints"
    
    params = {
        "datastreams": [
            {
                "id":"pi_info",
                "datapoints":[
                    {
                        "at": "",
                        "value": {
                            "CPUUsages": get_cpu_usage_percent(),
                            "IntranetIP": get_intranet_ip(),
                            "InternetIP": get_internet_ip(),
                            "MemoryFree": memory_info['mem_free'],
                            "MemoryTotal": memory_info['mem_total'],
                            "MemoryUsage": memory_info['mem_usage_percent']
                        }
                    }
                ]
            }
        ]
    }
    headers = {
        "api-key": "1PcrpnQa9gObx1ODmbMyevIYLeU=",
        "Centent-type": "application/json"        
    }
    
    response = requests.post(url,json=params,headers=headers)
    
    return response.text

while True:
    print("begin\n")
    memory_info = get_memory_info()
    print('mem_total(G):',memory_info['mem_total'])
    print('mem_free(G):',memory_info['mem_free'])
    print('mem_usage_percent(G):',memory_info['mem_usage_percent'])
    print('CPUUsages(%):',get_cpu_usage_percent())
    print('IntranetIP:',get_intranet_ip())
    print('InternetIP:',get_internet_ip())
    
    
    resp = sent_to_iot_platform(memory_info)
    
    print ("OneNET_result: %s" %resp)
    
    
    

    

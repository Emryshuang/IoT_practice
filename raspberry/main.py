import json,time

import ArduinoUSB as arduino
import Cloud as cloud

api_keyPI = "05Soo9nrtyrrAmkvdMCeTD6dY=A="
urlPI = "579733429"
idPI = "pi_data"
api_keylight = "CNgMBPfpv66FaWYndFyQ8OaFQ8="  #wrong
#api_keylight = "CNgMBPfpv66FaWYxndFyQ8OaFQ8="
urllight = "579733640"
idlight = "light_data"

def main():
    usb = arduino.USBInterface()
   # print("begin\n")
    onenetPI=cloud.Cloud(api_keyPI,urlPI,idPI)
    onenetlight=cloud.Cloud(api_keylight,urllight,idlight)
    usb.put_info("I am raspbeey\n".encode('utf-8'))
    time.sleep(5)
    
    while 1:
        usb.ser.flushOutput()
        usb.put_info("I am raspbeey\n".encode('utf-8'))
        str=usb.get_info()
        print(str)
        dic=eval(str)
        print(dic)
        print(type(dic))
        time.sleep(5)

        datalight=dic['light']
#        del dic['light']

               
        print("datas constructed\n")
        print(dic)         
        print(datalight)
        
        onenetPI.print_info()
        rep = onenetPI.sent_to_iot_platform(dic)
        print(rep+"\n")
        onenetlight.print_info()
        rep = onenetlight.sent_to_iot_platform(datalight)
        print(rep+"\n")
        print("end\n")
        
        time.sleep(5)
                
    

if __name__ == '__main__':
    main()
    
    

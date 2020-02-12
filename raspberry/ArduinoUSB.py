import serial,time,json

class USBInterface(object):
  def __init__(self):
    try:
      self.ser = serial.Serial('/dev/ttyACM1',9600)
      print("A serial Echo Is Running...\n")
    except Exception as e:
      print("open serial failed")


  def get_info(self):
    usb_str = ''
    s = self.ser.readline()
    
    print("usb receice: " + s.decode('utf-8'))
    return s
  
  def put_info(self,info):
    try:
        self.ser.write(info)
        print("usb put: " + info.decode('utf-8'))
    except Exception as e:
        print('failed to put')


        

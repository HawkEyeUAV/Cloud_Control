#!
# -*- coding: utf-8 -*-    
import paho.mqtt.client as mqtt   
import json  
�  
def on_connect(client, userdata, flags, rc):  
    print("Connected with result code " + str(rc))  
    client.subscribe("gpio")  
  
def on_message(client, userdata, msg):  
    print(msg.topic+" "+str(msg.payload))  
    # 获得负载中的pin 和 value  
  
if __name__ == '__main__':  
    client = mqtt.Client()  
    client.on_connect = on_connect  
    client.on_message = on_message  
    gpio_setup()  
      
    try:  
        # 请根据实际情况改变MQTT代理服务器的IP地址  
        client.connect("127.0.01", 1883, 60)  
        client.loop_forever()  
    except KeyboardInterrupt:  
        client.disconnect()  
        gpio_destroy()  

#!/usr/bin/env python
#encoding:utf-8    
import paho.mqtt.client as mqtt   
import json  
import time
import re
import MySQLdb as mdb
import sys
�  
def on_connect(client, userdata, flags, rc):  
    print("Connected with result code " + str(rc))  
    client.subscribe("gpio")  
  
def on_message(client, userdata, msg):  
    print(msg.topic+" "+str(msg.payload))  
    # 获得负载中的pin 和 value  
    con = mdb.connect('127.0.0.1','root','19950419li','tencentcloud')
        cur = con.cursor()
        cur.execute('INSERT INTO home(id,updatetime,tem,hum,distance) VALUES(null,null,%s,%s,%s)',c)
        con.commit()
        cur.close()
        con.close() 
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

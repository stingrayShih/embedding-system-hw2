#!/usr/bin/env python3
import socket
import numpy as np
import json
import time
import random
HOST = '192.168.73.11' # Standard loopback interface address
PORT = 8080 # Port to listen on (use ports > 1023)



accx=[]
accy=[]
accz=[]
magx=[]
magy=[]
magz=[]
gyrox=[]
gyroy=[]
gyroz=[]
temp=[]
humid=[]
pre=[]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
          
          data = conn.recv(1024).decode('utf-8')
          if data=='':
              break
          print('Received from socket server : ', data)
          
          tmp1=data.strip('|')
          datalist=tmp1.split('|')
          print(datalist)
          for i in datalist:
            if 'ax' in i:
              al=i.strip('{').strip('}').split(',')
              accx.append(float(al[0].strip("\"ax \": ")))
              accy.append(float(al[1].strip("\"ay \": ")))
              accz.append(float(al[2].strip("\"az \": ")))
            elif 'mx' in i:
              ml=i.strip('{').strip('}').split(',')
              magx.append(float(ml[0].strip("\"mx \": ")))
              magy.append(float(ml[1].strip("\"my \": ")))
              magz.append(float(ml[2].strip("\"mz \": ")))
            elif 'gx' in i:
              gl=i.strip('{').strip('}').split(',')
              gyrox.append(float(gl[0].strip("\"gx \": ")))
              gyroy.append(float(gl[1].strip("\"gy \": ")))
              gyroz.append(float(gl[2].strip("\"gz \": ")))
            elif 'temperature' in i:
              temp.append(float(i.strip('temperature=')))
            elif 'humidity' in i:
              humid.append(float(i.strip('humidity=')))
            elif 'pressure' in i:
              pre.append(float(i.strip('pressure=')))
              
              

s.close()



import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
xaxis=range(100)




# 把資料放進來並指定對應的X軸、Y軸的資料，用方形做標記(s-)，並指定線條顏色為紅色，使用label標記線條含意

plt.plot(xaxis,accx,'s-',color = 'r', label="accx")

# 把資料放進來並指定對應的X軸、Y軸的資料 用圓形做標記(o-)，並指定線條顏色為綠色、使用label標記線條含意

plt.plot(xaxis,accy,'o-',color = 'g', label="accy")

plt.plot(xaxis,accz,'^-',color = 'b', label="accz")

# 設定圖片標題，以及指定字型設定，x代表與圖案最左側的距離，y代表與圖片的距離

plt.title("acceleration", x=0.5, y=1.03)

# 设置刻度字体大小

plt.xticks(fontsize=20)

plt.yticks(fontsize=20)

# 標示x軸(labelpad代表與圖片的距離)

plt.xlabel("sample_num", fontsize=30, labelpad = 15)

# 標示y軸(labelpad代表與圖片的距離)

plt.ylabel("a", fontsize=30, labelpad = 20)

# 顯示出線條標記位置

plt.legend(loc = "best", fontsize=20)

# 畫出圖片

plt.show()

#mag


# 把資料放進來並指定對應的X軸、Y軸的資料，用方形做標記(s-)，並指定線條顏色為紅色，使用label標記線條含意

plt.plot(xaxis,magx,'s-',color = 'r', label="magx")

# 把資料放進來並指定對應的X軸、Y軸的資料 用圓形做標記(o-)，並指定線條顏色為綠色、使用label標記線條含意

plt.plot(xaxis,magy,'o-',color = 'g', label="magy")

plt.plot(xaxis,magz,'^-',color = 'b', label="magz")

# 設定圖片標題，以及指定字型設定，x代表與圖案最左側的距離，y代表與圖片的距離

plt.title("mag", x=0.5, y=1.03)

# 设置刻度字体大小

plt.xticks(fontsize=20)

plt.yticks(fontsize=20)

# 標示x軸(labelpad代表與圖片的距離)

plt.xlabel("sample_num", fontsize=30, labelpad = 15)

# 標示y軸(labelpad代表與圖片的距離)

plt.ylabel("mag", fontsize=30, labelpad = 20)

# 顯示出線條標記位置

plt.legend(loc = "best", fontsize=20)

# 畫出圖片

plt.show()

#gyro


# 把資料放進來並指定對應的X軸、Y軸的資料，用方形做標記(s-)，並指定線條顏色為紅色，使用label標記線條含意

plt.plot(xaxis,gyrox,'s-',color = 'r', label="gyrox")

# 把資料放進來並指定對應的X軸、Y軸的資料 用圓形做標記(o-)，並指定線條顏色為綠色、使用label標記線條含意

plt.plot(xaxis,gyroy,'o-',color = 'g', label="gyroy")

plt.plot(xaxis,gyroz,'^-',color = 'b', label="gyroz")

# 設定圖片標題，以及指定字型設定，x代表與圖案最左側的距離，y代表與圖片的距離

plt.title("gyro", x=0.5, y=1.03)

# 设置刻度字体大小

plt.xticks(fontsize=20)

plt.yticks(fontsize=20)

# 標示x軸(labelpad代表與圖片的距離)

plt.xlabel("sample_num", fontsize=30, labelpad = 15)

# 標示y軸(labelpad代表與圖片的距離)

plt.ylabel("gyro", fontsize=30, labelpad = 20)

# 顯示出線條標記位置

plt.legend(loc = "best", fontsize=20)

# 畫出圖片

plt.show()



#temperature


# 把資料放進來並指定對應的X軸、Y軸的資料，用方形做標記(s-)，並指定線條顏色為紅色，使用label標記線條含意

plt.plot(xaxis,temp,'s-',color = 'r', label="temp")


plt.title("temperature", x=0.5, y=1.03)

# 设置刻度字体大小

plt.xticks(fontsize=20)

plt.yticks(fontsize=20)

# 標示x軸(labelpad代表與圖片的距離)

plt.xlabel("sample_num", fontsize=30, labelpad = 15)

# 標示y軸(labelpad代表與圖片的距離)

plt.ylabel("degC", fontsize=30, labelpad = 20)

# 顯示出線條標記位置

plt.legend(loc = "best", fontsize=20)

# 畫出圖片

plt.show()

#humidity


# 把資料放進來並指定對應的X軸、Y軸的資料，用方形做標記(s-)，並指定線條顏色為紅色，使用label標記線條含意

plt.plot(xaxis,humid,'s-',color = 'r', label="humidity")


plt.title("humidity", x=0.5, y=1.03)

# 设置刻度字体大小

plt.xticks(fontsize=20)

plt.yticks(fontsize=20)

# 標示x軸(labelpad代表與圖片的距離)

plt.xlabel("sample_num", fontsize=30, labelpad = 15)

# 標示y軸(labelpad代表與圖片的距離)

plt.ylabel("", fontsize=30, labelpad = 20)

# 顯示出線條標記位置

plt.legend(loc = "best", fontsize=20)

# 畫出圖片

plt.show()

#pressure


# 把資料放進來並指定對應的X軸、Y軸的資料，用方形做標記(s-)，並指定線條顏色為紅色，使用label標記線條含意

plt.plot(xaxis,temp,'s-',color = 'r', label="pressure")


plt.title("pressure", x=0.5, y=1.03)

# 设置刻度字体大小

plt.xticks(fontsize=20)

plt.yticks(fontsize=20)

# 標示x軸(labelpad代表與圖片的距離)

plt.xlabel("sample_num", fontsize=30, labelpad = 15)

# 標示y軸(labelpad代表與圖片的距離)

plt.ylabel("mbar", fontsize=30, labelpad = 20)

# 顯示出線條標記位置

plt.legend(loc = "best", fontsize=20)

# 畫出圖片

plt.show()


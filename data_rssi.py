from cmath import log, sqrt
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

Telemetriler = pd.read_csv("test.csv")

rssi = Telemetriler.iloc[:,1].values
mac_address = Telemetriler.iloc[:,0].values

rssi_mac_d868=[]
rssi_mac_1cd6=[]
rssi_mac_3b86=[]
rssi_mac_28e8=[]
rssi_mac_d929=[]

print(rssi)
print(mac_address)

for i in range(len(rssi)):
    if(mac_address[i] == "A0:E6:F8:3F:D8:68"):
       rssi_mac_d868.append(rssi[i])
    elif(mac_address[i] == "A0:E6:F8:40:3B:86"):
        rssi_mac_3b86.append(rssi[i])
    elif(mac_address[i] == "A0:E6:F8:2C:1C:D6"):
        rssi_mac_1cd6.append(rssi[i])
    elif(mac_address[i] == "A0:E6:F8:40:28:E8"):
        rssi_mac_28e8.append(rssi[i])
    elif(mac_address[i] == "A0:E6:F8:3F:D9:29"):
        rssi_mac_d929.append(rssi[i])


#log_rssi_mac_3b86 = [log(y,10)for y in rssi_mac_3b86]
#root_rssi_mac_3b86 = [sqrt(abs(y))for y in rssi_mac_3b86]

fig, axs = plt.subplots(2,2)
axs[0,0].hist(rssi_mac_3b86,edgecolor="black",linewidth=1.2)
axs[0,0].set_title("3B:86")
axs[1,0].hist(rssi_mac_d868,edgecolor="black",linewidth=1.2)
axs[1,0].set_title("D8:68")
axs[0,1].hist(rssi_mac_1cd6,edgecolor="black",linewidth=1.2)
axs[0,1].set_title("1C:D6")
axs[1,1].hist(rssi_mac_28e8,edgecolor="black",linewidth=1.2)
axs[1,1].set_title("28:E8")

plt.show()


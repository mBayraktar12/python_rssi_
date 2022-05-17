from cmath import log
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer


Telemetriler = pd.read_csv("Experiments_Measurements.csv")

rssi = Telemetriler.iloc[:, :-1].values
mac_address = rssi[0, :]
print(type(mac_address))
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(rssi[1:, :])
rssi[1:, :] = imputer.transform(rssi[1:, :])

print(rssi)

for i in range(np.size(rssi, 1)):

    plt.subplot(1, 2, 1)
    plt.plot(rssi[2:, i], "ro", scalex=1, scaley=1)
    plt.subplot(1, 2, 2)
    plt.hist(rssi[2:, i],edgecolor = "black",linewidth = 1.2)
    plt.title(mac_address[i])
    plt.xlabel("RSSI")
    plt.ylabel("Freq")
    plt.show()

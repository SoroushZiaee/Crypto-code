import numpy as np
import talib
import matplotlib.pyplot as plt

# close = np.random.random(100)
# print(close)

# # Calculate the moving Average
# moving_average = talib.SMA(close, timeperiod=10)
# print(moving_average)

my_data = np.genfromtxt('15minutes.csv', delimiter=',')
close = my_data[:, 4]
print(close)

rsi = talib.RSI(close, timeperiod=5)
print(rsi)

plt.plot(rsi)
plt.grid(True)
plt.show()
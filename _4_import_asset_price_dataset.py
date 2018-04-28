import sys
import pandas as pd
import numpy as np
import _0_configurations as conf

reload(sys)
sys.setdefaultencoding('utf8')

data = pd.read_csv('input/EURUSD 1min.txt', names=['date','time','open','high','low','close','volume'])

data['datetime'] = pd.to_datetime(data['date'] + ' ' + data['time'], format='%d/%m/%Y %H:%M')

print(data.head())

# data['datetime'] = pd.to_datetime(data['datetime'], format='%Y-%m-%d %H:%M:%S')

data['Timestamp'] = data.datetime.values.astype(np.int64) // 10 ** 9

data.to_csv('input/EURUSD 1min_with_timestamp.csv', index=False)

print(data.head())

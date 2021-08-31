import config, csv
from kucoin.client import Client
import time, datetime
import pytz, dateparser


def return_timestamp(data):
    return int(time.mktime(datetime.datetime.strptime(data, '%Y-%m-%d').timetuple()))


client = Client(config.API_KEY, config.API_SECRET, config.API_PASSPHRASE)

candles = client.get_kline_data(symbol='BTC-USDT', kline_type='5min', start=return_timestamp('2017-01-01'), end=return_timestamp('2018-01-05'))[::-1]

with open('5minutes.csv', 'w', newline='') as fout:
    candlestick_writer = csv.writer(fout, delimiter=',')
    for candle in candles:
        candlestick_writer.writerow(candle)

print(len(candles))



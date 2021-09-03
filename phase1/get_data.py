import config, csv
from kucoin.client import Client
import time, datetime
import pytz, dateparser


def return_timestamp(data):
    return int(time.mktime(datetime.datetime.strptime(data, '%Y-%m-%d').timetuple()))


client = Client(config.API_KEY, config.API_SECRET, config.API_PASSPHRASE)

candles = client.get_kline_data(symbol='BTC-USDT', kline_type='5min')[::-1]

with open('5minutes-kucoin.csv', 'w', newline='') as fout:
    candlestick_writer = csv.writer(fout, delimiter=',')
    for candle in candles:
        candlestick_writer.writerow(candle)

print(len(candles))




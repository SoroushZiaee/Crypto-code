import numpy as np 
import yfinance as yf
import plotly.graph_objects as go


data = yf.download('BTC-USD',period='1d', interval='5m')

data.to_csv('5min-yfinance.csv', sep=',')

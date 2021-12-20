import websocket
import json
import pprint
import numpy as np
import talib
from talib import stream

symbol = "ethusdt"
interval = "1m"
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
SOCKET = f"wss://stream.binance.com:9443/ws/{symbol}@kline_{interval}"
IN_POSITION = False
CLOSED_PRICE = [3012.49109452, 3006.57246131, 3018.27175691, 3019.56576279,
                3011.89895092, 3000.12762449, 3010.65883013, 3019.97469986,
                3000.3518127, 3001.42923699, 3004.60835797, 3000.53194521,
                3016.67844692, 3013.57281035]


def on_open(ws):
    print("opened connection")


def on_close(ws):
    print("closed connection")


def is_candle_closed(json_message: dict) -> bool:
    return json_message["k"]["x"]


def on_message(ws, message):
    print("received message")
    json_message = json.loads(message)
    if is_candle_closed(json_message):
        pprint.pprint(f"Cloesed price : {json_message['k']['c']}")
        CLOSED_PRICE.append(float(json_message['k']['c']))
        print(f"The Close Price Len : {len(CLOSED_PRICE)}")

        if len(CLOSED_PRICE) > RSI_PERIOD:
            np_closed = np.array(CLOSED_PRICE)
            pprint.pprint(np_closed)
            print("Here")

            # For calculating the RSI faster for streaming the data we use the stream here instead talib
            rsi = talib.RSI(np_closed, RSI_PERIOD)
            print('-'*10 + "rsi" + '-'*10)
            pprint.pprint(rsi)
            last_rsi = rsi[-1]
            print(f"\t-the last rsi is : {last_rsi}")

            if last_rsi > RSI_OVERBOUGHT:
                if IN_POSITION:
                    print("we are in position, don't do anything")
                else:
                    print("\t-Signal : SELL")

            elif last_rsi < RSI_OVERSOLD:
                if IN_POSITION:
                    print("we are in position, don't do anything")
                else:
                    print("\t-Signal : BUY")


ws = websocket.WebSocketApp(SOCKET, on_open=on_open,
                            on_close=on_close, on_message=on_message)
ws.run_forever()

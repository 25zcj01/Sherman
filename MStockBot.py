#!/usr/bin/python3

import alpaca_trade_api as tradeapi
import time
import datetime

print("\033c")

def time_to_market_close():
    clock = api.get_clock()
    return (clock.next_close - clock.timestamp).total_seconds()


def wait_for_market_open():
    clock = api.get_clock()
    if not clock.is_open:
        print("Market opens: " + str(clock.next_open))
        print()
        print("Sleeping...")
        time_to_open = (clock.next_open - clock.timestamp).total_seconds()
        time.sleep(round(time_to_open))

hours = [9, 10, 11, 12, 13, 14, 15, 16, 16]
key = "my_key"
sec = "my_sec_key"

url = "https://paper-api.alpaca.markets"

api = tradeapi.REST(key, sec, url, api_version='v2')

account = api.get_account()

while True:
    current_time = datetime.datetime.now()
    hour = int(current_time.strftime('%H'))
    
    while hour in hours:
        print("\033c")
        print(account.status)
        if time_to_market_close() > 300:
            n = 0
            symbols = ["FB", "AAPL", "GOOG"]
            stockqty = ["30", "50", "20"]
            percent = 0.5
            percentN = -percent
            count = 0
            while True:
                n = 0
                for i in range(len(symbols)):
                    barset = api.get_barset(symbols[n], "minute",)
                    symbols_bars = barset[symbols[n]]
                    minute_open = symbols_bars[0].o
                    minute_open2 = symbols_bars[-1].o
                    percent_change = (minute_open2 - minute_open) / minute_open * 100

                    try:
                        position = api.get_position(symbols[n])
                    except:
                        api.submit_order(
                                    symbol=symbols[n],
                                    qty="1",
                                    side="buy",
                                    type="market",
                                    time_in_force="day"
                                )
                        time.sleep(10)
                    position = api.get_position("AAPL")
                    print(f"Current balance: ${account.equity}")
                    print(f"You have {position.qty} shares of " + symbols[n])
                    
                time1 = str(time)

                if int(round(percent_change, 2)) >= percent and int(position.qty) == (int(stockqty[n]) + 1):
                    api.submit_order(
                                symbol=symbols[n],
                                qty=stockqty[n],
                                side="sell",
                                type="market",
                                time_in_force="day"
                            )
                    update = open("Mupdates.txt", "a")
                    update.write("MSherman sold " + stockqty[n] + " of " + symbols[n] + " for " + minute_open + " each.")
                    update.close()

                    print("MSherman sold " + stockqty[n] + " of " + symbols[n] + " for " + minute_open + " each.")
                    print()

                elif int(round(percent_change, 2) <= percentN and int(position.qty) == 1:
                    api.submit_order(
                                symbol=symbols[n],
                                qty=stockqty[n],
                                side="buy",
                                type="market",
                                time_in_force="day",
                            )
                    update = open("Mupdates.txt", "a")
                    update.write("MSherman bought " + stockqty[n] + " of " + symbols[n] + " for " + minute_open + " each.")
                    update.close()

                    print("MSherman bought " + stockqty[n] + " of " + symbols[n] + " for " + minute_open + " each.")
                    print()
                    
                n += 1
                time.sleep(10)

        updates = open("Mupdates.txt", "r")
        lines = upadtes.readlines()
        for line in lines:
            count += 1
            print(f"Line {count}: " + line.strip())
        wait_for_market_open()
                    

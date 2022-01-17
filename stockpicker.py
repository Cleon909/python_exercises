#python scripte to pick the biggest difference between a set f values with the lowest value coming first

def stock_picker(prices):
    dic = {}
    for buy_day,buy_price in enumerate(prices):
        for sell_day, sell_price in enumerate(prices):
            if sell_day > buy_day:
                dic["{},{}".format(buy_day,sell_day)] = sell_price - buy_price

    pick = []
    pick.append(max(dic,key=dic.get))
    values = dic.values()
    pick.append(max(values))

    print("day to buy and day to sell = {}. profit = {}".format(pick[0],pick[1]))

stock_picker([100, 2, 5, 500, 4, 10, 1])
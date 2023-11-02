def solution():
    
    cameras_bought = 3
    buy_price = 20
    maddox_sell_price = 28
    theo_sell_price = 23

    maddox_profit = (maddox_sell_price - buy_price) * cameras_bought
    theo_profit = (theo_sell_price - buy_price) * cameras_bought

    profit_difference = maddox_profit - theo_profit
    result = profit_difference
    return result

print(solution())
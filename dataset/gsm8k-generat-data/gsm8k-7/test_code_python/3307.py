def solution():
    natasha_money = 60
    carla_money = natasha_money / 3
    cosima_money = carla_money / 2

    total_money = natasha_money + carla_money + cosima_money

    buying_price = total_money
    selling_price = (7/5) * buying_price

    profit = selling_price - buying_price
    result = profit
    return result

print(solution())
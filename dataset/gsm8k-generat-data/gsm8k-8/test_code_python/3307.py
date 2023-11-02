def solution():
    # Calculate the amount of money Carla and Cosima have
    natasha_money = 60
    carla_money = natasha_money / 3
    cosima_money = carla_money / 2

    # Calculate the total amount of money they have
    total_money = natasha_money + carla_money + cosima_money

    # Calculate the buying price and selling price of the goods they buy
    buying_price = total_money
    selling_price = (7/5) * buying_price

    # Calculate the profit they make
    profit = selling_price - buying_price
    result = profit
    return result

print(solution())
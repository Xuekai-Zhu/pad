def solution():
    """Natasha has 3 times as much money as Carla, and Carla has twice as much money as Cosima. If Natasha has $60, and the three decide to buy goods worth the total amount they have and sell the goods at 7/5 of the buying price, how much profit would they make?"""
    # Calculate the amount of money Natasha, Carla, and Cosima have
    natasha_money = 60
    carla_money = natasha_money / 3
    cosima_money = carla_money / 2

    # Calculate the total amount of money they have to buy goods
    total_money = natasha_money + carla_money + cosima_money

    # Calculate the buying price of the goods
    buying_price = total_money

    # Calculate the selling price of the goods
    selling_price = (7/5) * buying_price

    # Calculate the profit they would make
    profit = selling_price - buying_price

    result = profit
    return result

print(solution())
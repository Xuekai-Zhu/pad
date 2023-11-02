def solution():
    """Natasha has 3 times as much money as Carla, and Carla has twice as much money as Cosima. If Natasha has $60, and the three decide to buy goods worth the total amount they have and sell the goods at 7/5 of the buying price, how much profit would they make?"""
    natasha_money = 60
    carla_money = natasha_money / 3
    cosima_money = carla_money / 2
    total_money = natasha_money + carla_money + cosima_money
    buying_price = total_money
    selling_price = 7/5 * buying_price
    profit = selling_price - buying_price
    result = profit
    return result

print(solution())
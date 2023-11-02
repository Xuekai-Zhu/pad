def solution():
    """Peter goes to the store to buy a soda. The soda costs $.25 an ounce. He brought $2 with him and leaves with $.50. How many ounces of soda did he buy?"""
    initial_money = 2
    final_money = 2.5
    soda_price_per_ounce = 0.25
    total_soda_ounces = (initial_money - final_money) / soda_price_per_ounce
    result = total_soda_ounces
    return result

print(solution())
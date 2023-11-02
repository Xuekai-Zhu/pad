def solution():
    """Peter goes to the store to buy a soda. The soda costs $.25 an ounce. He brought $2 with him and leaves with $.50. How many ounces of soda did he buy?"""
    initial_money = 2
    final_money = .5
    total_spent = initial_money - final_money
    cost_per_ounce = .25
    total_ounces = total_spent / cost_per_ounce
    result = total_ounces
    return result

print(solution())
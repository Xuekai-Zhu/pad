def solution():
    """Peter goes to the store to buy a soda. The soda costs $.25 an ounce. He brought $2 with him and leaves with $.50. How many ounces of soda did he buy?"""
    cost_per_ounce = 0.25
    money_brought = 2
    money_left = 0.50
    cost_of_soda = money_brought - money_left
    ounces_bought = cost_of_soda / cost_per_ounce
    result = ounces_bought
    return result

print(solution())
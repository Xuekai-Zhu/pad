def solution():
    """Mom went shopping at the market. She left with €55. She bought 2 packs of bananas for €4 each, pears for €2, asparagus for €6 and finally a chicken for €11. How much money does Mom have left?"""
    # Define the initial amount of money Mom had
    initial_money = 55

    # Define the cost of bananas, pears, asparagus, and chicken
    bananas_cost = 4 * 2
    pears_cost = 2
    asparagus_cost = 6
    chicken_cost = 11

    # Calculate the total cost of Mom's shopping
    total_cost = bananas_cost + pears_cost + asparagus_cost + chicken_cost

    # Calculate the amount of money Mom has left
    money_left = initial_money - total_cost

    # Return the amount of money Mom has left
    result = money_left
    return result

print(solution())
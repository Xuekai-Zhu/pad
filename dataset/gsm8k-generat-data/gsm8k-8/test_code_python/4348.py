def solution():
    # Calculate the total cost of the ducks
    duck_cost = 30 * 10

    # Calculate the total weight of the ducks
    duck_weight = 30 * 4

    # Calculate the total income from selling the ducks
    duck_income = duck_weight * 5

    # Calculate the profit
    profit = duck_income - duck_cost
    result = profit
    return result

print(solution())
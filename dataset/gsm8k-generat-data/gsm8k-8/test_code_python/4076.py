def solution():
    # Calculate the number of goldfish that need special food
    special_fish = int(0.2 * 50)

    # Calculate the amount of special food needed in ounces
    special_food = special_fish * 1.5

    # Calculate the cost of the special food
    special_food_cost = special_food * 3

    result = special_food_cost
    return result

print(solution())
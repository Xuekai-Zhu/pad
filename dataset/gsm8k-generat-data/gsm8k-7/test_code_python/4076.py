def solution():
    num_goldfish = 50
    food_per_goldfish = 1.5 # ounces
    special_food_percentage = 0.2 # 20%

    # Calculate the number of goldfish that need special food
    num_special = int(num_goldfish * special_food_percentage)

    # Calculate the total amount of food needed per day
    total_food_per_day = num_goldfish * food_per_goldfish

    # Calculate the amount of special food needed per day
    special_food_per_day = num_special * food_per_goldfish

    # Calculate the cost of the special food per day
    special_food_cost_per_day = special_food_per_day * 3

    result = special_food_cost_per_day
    return result

print(solution())
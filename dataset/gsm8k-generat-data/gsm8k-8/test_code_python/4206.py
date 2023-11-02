def solution():
    # Calculate the total amount of special dog food needed during the first 60 days
    food_first_60_days = 2 * 60

    # Calculate the total amount of special dog food needed after the first 60 days
    food_after_60_days = 4 * (365 - 60)

    # Calculate the total amount of special dog food needed over the entire year
    total_food = food_first_60_days + food_after_60_days

    # Calculate the total weight of special dog food needed, in ounces
    total_weight_ounces = total_food * 16

    # Calculate the total number of 5-pound bags needed
    bags_needed = total_weight_ounces / (5 * 16)

    # Round up to the nearest whole number of bags
    bags_needed = math.ceil(bags_needed)

    result = bags_needed
    return result

print(solution())
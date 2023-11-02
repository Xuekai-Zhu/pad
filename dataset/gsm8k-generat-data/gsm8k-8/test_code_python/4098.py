def solution():
    # Calculate the amount of coffee she drinks in one day
    coffee_per_day = (20 - (0.5 * 8)) * 2 # 0.5 cup of milk and 8 ounces in a cup

    # Calculate the amount of coffee she drinks in one week
    coffee_per_week = coffee_per_day * 5

    # Calculate the amount of coffee she now drinks after reducing by 1/4
    new_coffee_per_week = coffee_per_week * 0.75

    result = new_coffee_per_week
    return result

print(solution())
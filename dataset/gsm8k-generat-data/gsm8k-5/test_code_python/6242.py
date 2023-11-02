def solution():
    bottles_per_day = 2  # Tim drinks 2 bottles per day
    bottle_size = 1.5  # Each bottle is 1.5 quarts
    ounces_per_day = 20  # Tim drinks an additional 20 ounces per day
    quarts_per_ounce = 0.03125  # 1 ounce is 0.03125 quarts
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total amount of water Tim drinks in quarts per day
    water_per_day = (bottles_per_day * bottle_size * 4) + (ounces_per_day * quarts_per_ounce)

    # Calculate the total amount of water Tim drinks in quarts per week
    water_per_week = water_per_day * days_per_week
    result = water_per_week
    return result

print(solution())
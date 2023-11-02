def solution():
    quarts_per_bottle = 1.5
    ounces_per_day = 20
    days_per_week = 7
    water_consumed = (quarts_per_bottle * 2) + (ounces_per_day / 4)
    water_consumed_per_week = water_consumed * days_per_week
    result = water_consumed_per_week
    return result

print(solution())
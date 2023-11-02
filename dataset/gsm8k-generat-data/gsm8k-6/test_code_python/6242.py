def solution():
    # Calculate the total amount of water Tim drinks in a day
    total_water_day = 2*1.5*32 + 20  # 2 bottles at 1.5 quarts each = 3 quarts = 96 ounces, plus 20 ounces

    # Calculate the total amount of water Tim drinks in a week
    total_water_week = total_water_day * 7

    result = total_water_week
    return result

print(solution())
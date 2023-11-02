def solution():
    num_gallons_per_day = 1.5
    num_quarts_per_gallon = 4

    num_days_per_week = 7

    # Calculate the total number of quarts John drinks in a week
    total_quarts_per_week = num_gallons_per_day * num_quarts_per_gallon * num_days_per_week
    result = total_quarts_per_week
    return result

print(solution())
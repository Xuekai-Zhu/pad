def solution():
    breakfast_intake = 560
    lunch_intake = 780
    dinner_intake = 0 # we haven't computed this yet
    cake_calories = 110
    chips_calories = 310
    coke_calories = 215
    daily_limit = 2500

    # Compute the total intake for dinner
    dinner_intake = cake_calories + chips_calories + coke_calories

    # Compute the total daily intake
    total_intake = breakfast_intake + lunch_intake + dinner_intake

    # Compute the remaining intake for the day
    remaining_intake = daily_limit - total_intake
    result = remaining_intake
    return result

print(solution())
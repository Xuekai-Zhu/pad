def solution():
    bear_daily_food = 90
    days_in_week = 7
    weeks = 3
    victor_weight = 126

    total_food_for_bear = bear_daily_food * days_in_week * weeks
    victors_worth_of_food = total_food_for_bear / victor_weight

    result = victors_worth_of_food
    return result

print(solution())
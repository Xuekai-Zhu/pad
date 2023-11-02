def solution():
    bear_food_per_day = 90
    victor_weight = 126
    days_in_3_weeks = 21

    # Calculate the total amount of food a bear would eat in 3 weeks
    total_bear_food = bear_food_per_day * days_in_3_weeks

    # Calculate how many "Victors" worth of food that is
    victor_ratio = total_bear_food / victor_weight
    result = victor_ratio
    return result

print(solution())
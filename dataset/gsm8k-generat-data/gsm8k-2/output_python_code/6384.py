def solution():
    """A bear eats up to 90 pounds of food per day to prepare for hibernation. If Victor weighs 126 pounds, how many "Victors" worth of food would a bear eat in 3 weeks?"""
    bear_food_per_day = 90
    victor_weight = 126
    victors_worth_of_food = bear_food_per_day / victor_weight
    total_days = 21
    total_food = bear_food_per_day * total_days
    total_victors = total_food / victor_weight / 3
    result = total_victors
    return result

print(solution())
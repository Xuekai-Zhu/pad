def solution():
    """A bear eats up to 90 pounds of food per day to prepare for hibernation. If Victor weighs 126 pounds, how many "Victors" worth of food would a bear eat in 3 weeks?"""
    food_per_day = 90
    weeks = 3
    days_per_week = 7
    victor_weight = 126
    total_food = food_per_day * days_per_week * weeks
    victors_worth_of_food = total_food / victor_weight
    result = victors_worth_of_food
    return result

print(solution())
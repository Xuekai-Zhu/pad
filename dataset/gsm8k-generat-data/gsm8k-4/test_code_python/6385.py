def solution():
    """A bear eats up to 90 pounds of food per day to prepare for hibernation. If Victor weighs 126 pounds, how many "Victors" worth of food would a bear eat in 3 weeks?"""
    # Define the amount of food a bear eats per day and the weight of Victor
    bear_food_per_day = 90
    victor_weight = 126

    # Calculate the amount of food a bear would eat in 3 weeks
    bear_food_3_weeks = bear_food_per_day * 7 * 3

    # Calculate the number of "Victors" worth of food the bear would eat in 3 weeks
    victors_worth_of_food = bear_food_3_weeks / victor_weight

    # Return the result
    result = victors_worth_of_food
    return result

print(solution())
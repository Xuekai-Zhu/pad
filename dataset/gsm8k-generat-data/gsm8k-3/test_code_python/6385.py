def solution():
    """A bear eats up to 90 pounds of food per day to prepare for hibernation. If Victor weighs 126 pounds, how many "Victors" worth of food would a bear eat in 3 weeks?"""
    
    # Define constants
    FOOD_PER_DAY = 90
    DAYS_PER_WEEK = 7
    WEEKS_PER_THREE_WEEKS = 3
    VICTOR_WEIGHT = 126

    # Calculate the total amount of food a bear eats in 3 weeks
    total_food = FOOD_PER_DAY * DAYS_PER_WEEK * WEEKS_PER_THREE_WEEKS

    # Calculate how many "Victors" worth of food a bear eats in 3 weeks
    victors_worth = total_food / VICTOR_WEIGHT

    # Display the result
    result = victors_worth
    return result

print(solution())
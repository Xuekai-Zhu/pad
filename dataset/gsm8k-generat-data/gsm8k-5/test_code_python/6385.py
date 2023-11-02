def solution():
    bear_food_per_day = 90  # A bear eats up to 90 pounds of food per day
    days_per_week = 7  # There are 7 days in a week
    weeks = 3  # The bear needs to eat for 3 weeks
    victor_weight = 126  # Victor weighs 126 pounds

    # Calculate the total amount of food the bear needs to eat in 3 weeks
    total_food = bear_food_per_day * days_per_week * weeks

    # Calculate the number of "Victors" worth of food the bear would eat
    victors_worth_of_food = total_food / victor_weight
    result = victors_worth_of_food
    return result

print(solution())
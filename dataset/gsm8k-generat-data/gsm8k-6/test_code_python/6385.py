def solution():
    # Calculate the amount of food a bear would eat in 3 weeks
    bear_food_per_day = 90
    bear_food_per_week = bear_food_per_day * 7 
    bear_food_in_three_weeks = bear_food_per_week * 3

    # Calculate how many "Victor's" worth of food a bear would eat in 3 weeks
    victors_worth_of_food = bear_food_in_three_weeks / 126
    result = victors_worth_of_food
    return result

print(solution())
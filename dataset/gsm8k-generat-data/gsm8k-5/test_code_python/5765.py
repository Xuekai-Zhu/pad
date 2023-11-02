def solution():
    # Calculate the food consumption in the first two weeks
    food_consumption_first_weeks = (1/4) * 3 * 7 * 2  # 1/4 cup of food, 3 times a day, 7 days a week, for 2 weeks
    # Calculate the food consumption in the next two weeks
    food_consumption_next_weeks = (1/2) * 2 * 7 * 2  # 1/2 cup of food, twice a day, 7 days a week, for 2 weeks
    # Calculate the food consumption for today
    food_consumption_today = 1/2  # Lily has already fed the puppy 1/2 cup of food today
    # Calculate the total food consumption over the next 4 weeks
    total_consumption = food_consumption_first_weeks + food_consumption_next_weeks + food_consumption_today
    result = total_consumption
    return result

print(solution())
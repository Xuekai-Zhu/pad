def solution():
    """Lily got a new puppy for her birthday. She was responsible for feeding the puppy 1/4 cup of food three times a day for two weeks starting tomorrow. For the following 2 weeks, Lily will feed him 1/2 cup of food twice a day. She has fed him 1/2 cup of food today. Including today, how much food will the puppy eat over the next 4 weeks?"""
    # Define the amount of food Lily feeds the puppy
    food_per_day_1 = 1/4
    food_per_day_2 = 1/2

    # Define the number of feedings per day for each period
    feedings_per_day_1 = 3
    feedings_per_day_2 = 2

    # Define the number of days for each period
    days_1 = 14
    days_2 = 14

    # Calculate the total amount of food for each period
    total_food_1 = food_per_day_1 * feedings_per_day_1 * days_1
    total_food_2 = food_per_day_2 * feedings_per_day_2 * days_2

    # Calculate the total amount of food for the entire 4-week period
    total_food = total_food_1 + total_food_2 + 0.5

    # Return the result
    result = total_food
    return result

print(solution())
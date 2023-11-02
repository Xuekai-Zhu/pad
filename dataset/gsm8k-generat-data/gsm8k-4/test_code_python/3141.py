def solution():
    """
    John eats 3 meals a day. Breakfast is 500 calories. His lunch contains 25% more calories than that.
    His dinner is twice as many calories as lunch. He also has 3 shakes that are each 300 calories.
    How many calories does he get in a day?
    """

    # Define the calories in breakfast, lunch, and dinner
    breakfast_calories = 500
    lunch_calories = breakfast_calories * 1.25
    dinner_calories = lunch_calories * 2

    # Define the calories in shakes
    shakes_calories = 3 * 300

    # Calculate the total calories John consumes in a day
    total_calories = (breakfast_calories + lunch_calories + dinner_calories) + shakes_calories

    result = total_calories
    return result

print(solution())
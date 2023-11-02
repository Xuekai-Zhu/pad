def solution():
    """John eats 3 meals a day.  Breakfast is 500 calories.  His lunch contains 25% more calories than that.  His dinner is twice as many calories as lunch.  He also has 3 shakes that are each 300 calories.  How many calories does he get in a day?"""
    # Define the number of calories in each meal
    BREAKFAST_CALORIES = 500
    LUNCH_CALORIES = 1.25 * BREAKFAST_CALORIES
    DINNER_CALORIES = 2 * LUNCH_CALORIES
    SHAKE_CALORIES = 300

    # Calculate the total number of calories from meals
    meal_calories = 3 * (BREAKFAST_CALORIES + LUNCH_CALORIES + DINNER_CALORIES)

    # Calculate the total number of calories from shakes
    shake_calories = 3 * SHAKE_CALORIES

    # Calculate the total number of calories
    total_calories = meal_calories + shake_calories

    # Display the total number of calories
    result = total_calories
    return result

print(solution())
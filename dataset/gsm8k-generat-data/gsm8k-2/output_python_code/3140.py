def solution():
    """John eats 3 meals a day. Breakfast is 500 calories. His lunch contains 25% more calories than that. His dinner is twice as many calories as lunch. He also has 3 shakes that are each 300 calories. How many calories does he get in a day?"""
    breakfast_calories = 500
    lunch_calories = 1.25 * breakfast_calories
    dinner_calories = 2 * lunch_calories
    total_meal_calories = breakfast_calories + lunch_calories + dinner_calories
    shakes_calories = 3 * 300
    total_calories = total_meal_calories + shakes_calories
    result = total_calories
    return result

print(solution())
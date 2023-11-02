def solution():
    """John eats 3 meals a day. Breakfast is 500 calories. His lunch contains 25% more calories than that. His dinner is twice as many calories as lunch. He also has 3 shakes that are each 300 calories. How many calories does he get in a day?"""
    breakfast_cal = 500
    lunch_cal = 1.25 * breakfast_cal
    dinner_cal = 2 * lunch_cal
    shakes_cal = 3 * 300
    total_cal = (breakfast_cal + lunch_cal + dinner_cal) * 3 + shakes_cal
    result = total_cal
    return result

print(solution())
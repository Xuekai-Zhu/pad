def solution():
    breakfast_calories = 500  # John's breakfast contains 500 calories
    lunch_calories = 1.25 * breakfast_calories  # John's lunch contains 25% more calories than breakfast
    dinner_calories = 2 * lunch_calories  # John's dinner has twice as many calories as lunch
    shake_calories = 3 * 300  # John has 3 shakes that are each 300 calories

    # Calculate the total number of calories John consumes in a day
    total_calories = (breakfast_calories + lunch_calories + dinner_calories) * 3 + shake_calories
    result = total_calories
    return result

print(solution())
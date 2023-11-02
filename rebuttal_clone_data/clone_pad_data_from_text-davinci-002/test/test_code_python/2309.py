def solution():
    cake_slices = 8
    cake_calories = 347
    brownie_slices = 6
    brownie_calories = 375
    total_cake_calories = cake_slices * cake_calories
    total_brownie_calories = brownie_slices * brownie_calories
    calories_difference = total_cake_calories - total_brownie_calories
    result = calories_difference
    return result

print(solution())
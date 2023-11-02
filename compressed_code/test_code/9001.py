def solution():
    
    cake_slices = 8
    cake_calories = 347 * cake_slices
    brownies_per_pan = 6
    brownie_calories = 375 * brownies_per_pan
    calorie_difference = cake_calories - brownie_calories
    result = calorie_difference
    return result

print(solution())
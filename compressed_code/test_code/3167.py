def solution():
    
    cake_slices = 8
    cake_calories_per_slice = 347
    brownies_slices = 6
    brownies_calories_per_slice = 375
    total_cake_calories = cake_slices * cake_calories_per_slice
    total_brownies_calories = brownies_slices * brownies_calories_per_slice
    difference = total_cake_calories - total_brownies_calories
    result = difference
    return result

print(solution())
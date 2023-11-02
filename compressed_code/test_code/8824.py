def solution():
    
    price_per_mushroom = 2
    mushrooms_first_day = 58 // price_per_mushroom
    mushrooms_second_day = 12
    mushrooms_third_day = mushrooms_second_day * 2
    total_mushrooms = mushrooms_first_day + mushrooms_second_day + mushrooms_third_day
    result = total_mushrooms
    return result

print(solution())
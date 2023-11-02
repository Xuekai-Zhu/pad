def solution():
    
    total_fruit_weight = 8  
    mario_oranges = 8 / 16  
    lydia_apples = 24 / 16  
    nicolai_peaches = total_fruit_weight - mario_oranges - lydia_apples
    result = nicolai_peaches
    return result

print(solution())
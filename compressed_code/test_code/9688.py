def solution():
    
    carrots = 1
    broccoli = 2
    carrot_calories = 51
    broccoli_calories_per_pound = carrot_calories / 3
    total_carrot_calories = carrots * carrot_calories
    total_broccoli_calories = broccoli * broccoli_calories_per_pound
    total_calories = total_carrot_calories + total_broccoli_calories
    result = total_calories
    return result

print(solution())
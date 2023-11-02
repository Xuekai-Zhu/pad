def solution():
    
    lettuce_calories = 30
    cucumber_calories = 80
    crouton_calories = 20
    crouton_count = 12
    total_calories = lettuce_calories + cucumber_calories + (crouton_calories * crouton_count)
    result = total_calories
    return result

print(solution())
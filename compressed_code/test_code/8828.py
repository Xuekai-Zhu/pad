def solution():
    
    total_calories = 2800
    calories_per_slice = 350
    eaten_percent = 0.25
    eaten_calories = total_calories * eaten_percent
    slices_eaten = eaten_calories / calories_per_slice
    result = slices_eaten
    return result

print(solution())
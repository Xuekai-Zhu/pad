def solution():
    num_slices = 8
    calories_per_slice = 300
    num_slices_eaten = num_slices / 2
    
    total_calories = num_slices_eaten * calories_per_slice
    result = total_calories
    return result

print(solution())
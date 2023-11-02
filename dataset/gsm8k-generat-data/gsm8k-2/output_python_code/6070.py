def solution():
    """Bob orders a pizza with 8 slices. He eats half of it and each slice was 300 calories. How many calories did he eat?"""
    total_slices = 8
    slices_eaten = total_slices / 2
    calories_per_slice = 300
    total_calories = slices_eaten * calories_per_slice
    result = total_calories
    return result

print(solution())
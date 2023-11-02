def solution():
    """Bob orders a pizza with 8 slices. He eats half of it and each slice was 300 calories. How many calories did he eat?"""
    slices = 8
    slices_eaten = slices / 2
    calories_per_slice = 300
    calories_eaten = slices_eaten * calories_per_slice
    result = calories_eaten
    return result

print(solution())
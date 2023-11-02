def solution():
    """Bob orders a pizza with 8 slices. He eats half of it and each slice was 300 calories. How many calories did he eat?"""
    # Define the number of slices in the pizza and the number of calories per slice
    slices = 8
    calorie_per_slice = 300

    # Calculate the number of slices Bob ate
    slices_eaten = slices / 2

    # Calculate the total number of calories Bob ate
    total_calories = slices_eaten * calorie_per_slice

    result = total_calories
    return result

print(solution())
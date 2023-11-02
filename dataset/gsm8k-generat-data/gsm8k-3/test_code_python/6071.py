def solution():
    """Bob orders a pizza with 8 slices.  He eats half of it and each slice was 300 calories.  How many calories did he eat?"""
    # Define the number of slices in a pizza and the calories per slice
    SLICES_PER_PIZZA = 8
    CALORIES_PER_SLICE = 300

    # Calculate the number of slices Bob ate
    slices_ate = SLICES_PER_PIZZA / 2

    # Calculate the total number of calories Bob ate
    total_calories = slices_ate * CALORIES_PER_SLICE

    # Display the total number of calories Bob ate
    result = total_calories
    return result

print(solution())
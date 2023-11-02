def solution():
    pizza_slices = 8
    calories_per_slice = 300

    # Calculate the total number of calories in the entire pizza
    total_calories = pizza_slices * calories_per_slice

    # Calculate the number of slices Bob ate
    slices_eaten = pizza_slices / 2

    # Calculate the total number of calories Bob ate
    calories_eaten = slices_eaten * calories_per_slice
    result = calories_eaten
    return result

print(solution())
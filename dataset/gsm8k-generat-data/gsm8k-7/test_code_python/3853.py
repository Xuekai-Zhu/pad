def solution():
    calorie_per_slice = 350
    total_calories = 2800
    portion_eaten = 0.25

    # Calculate the total calories Kiley ate
    calories_eaten = total_calories * portion_eaten

    # Calculate the number of slices Kiley ate
    slices_eaten = calories_eaten / calorie_per_slice
    result = slices_eaten
    return result

print(solution())
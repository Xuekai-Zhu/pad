def solution():
    total_slices = 8  # Bob orders a pizza with 8 slices
    slices_eaten = total_slices / 2  # Bob eats half of the pizza
    calories_per_slice = 300  # Each slice has 300 calories

    # Calculate the total number of calories Bob ate
    total_calories = slices_eaten * calories_per_slice

    result = total_calories
    return result

print(solution())
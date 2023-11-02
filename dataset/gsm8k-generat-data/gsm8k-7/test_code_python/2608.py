def solution():
    slices_per_sandwich = 3
    current_slices = 31
    sandwiches_to_make = 50

    # Calculate how many slices of ham are needed to make all the sandwiches
    total_slices_needed = sandwiches_to_make * slices_per_sandwich

    # Calculate how many more slices of ham are needed
    slices_needed = total_slices_needed - current_slices
    result = slices_needed
    return result

print(solution())
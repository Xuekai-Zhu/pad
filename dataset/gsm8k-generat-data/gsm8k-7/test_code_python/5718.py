def solution():
    slices_per_sandwich = 2
    days_of_week = 7
    extra_sandwiches = 2
    starting_slices = 22

    # Calculate the total number of sandwiches Tony made
    total_sandwiches = (days_of_week * slices_per_sandwich) + extra_sandwiches

    # Calculate the number of slices of bread used for all the sandwiches
    total_slices_used = total_sandwiches * slices_per_sandwich

    # Calculate the number of slices of bread remaining
    slices_remaining = starting_slices - total_slices_used

    result = slices_remaining
    return result

print(solution())
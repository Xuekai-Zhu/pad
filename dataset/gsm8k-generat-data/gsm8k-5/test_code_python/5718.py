def solution():
    slices_per_sandwich = 2  # Tony uses 2 slices of bread per sandwich
    sandwiches_per_week = 7  # Tony makes a sandwich every day of the week
    extra_sandwiches = 2  # Tony made 2 extra sandwiches on Saturday
    total_sandwiches = sandwiches_per_week + extra_sandwiches  # Total number of sandwiches Tony made this week
    total_slices_used = total_sandwiches * slices_per_sandwich  # Total number of slices of bread used
    slices_left = 22 - total_slices_used  # Calculate the number of slices of bread remaining
    result = slices_left
    return result

print(solution())
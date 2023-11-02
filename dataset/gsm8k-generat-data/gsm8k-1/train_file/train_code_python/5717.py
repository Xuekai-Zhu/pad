def solution():
    """Tony made a sandwich with two slices of bread for lunch every day this week. On Saturday, he was extra hungry from doing yard work and made two sandwiches. How many slices of bread are left from the 22-slice loaf Tony started with?"""
    slices_per_sandwich = 2
    sandwiches_per_day = 1
    days_per_week = 6
    extra_sandwiches = 2
    starting_slices = 22
    total_sandwiches = sandwiches_per_day * days_per_week + extra_sandwiches
    total_slices_used = total_sandwiches * slices_per_sandwich
    slices_left = starting_slices - total_slices_used
    result = slices_left
    return result

print(solution())
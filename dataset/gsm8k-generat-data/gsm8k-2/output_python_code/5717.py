def solution():
    """Tony made a sandwich with two slices of bread for lunch every day this week. On Saturday, he was extra hungry from doing yard work and made two sandwiches. How many slices of bread are left from the 22-slice loaf Tony started with?"""
    bread_slices_per_sandwich = 2
    sandwiches_per_day = 1
    extra_sandwiches_on_Saturday = 2
    total_sandwiches = (sandwiches_per_day * 6) + extra_sandwiches_on_Saturday
    remaining_slices = 22 - (total_sandwiches * bread_slices_per_sandwich)
    result = remaining_slices
    return result

print(solution())
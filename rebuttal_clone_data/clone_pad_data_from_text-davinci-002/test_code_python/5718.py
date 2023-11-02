def solution():
    slices_per_sandwich = 2
    sandwiches_made = 7
    extra_sandwiches = 2
    total_slices_used = (slices_per_sandwich * sandwiches_made) + (extra_sandwiches * slices_per_sandwich)
    result = 22 - total_slices_used
    return result

print(solution())
def solution():
    sandwiches_eaten_Saturday = 2
    sandwiches_eaten_Sunday = 1
    slices_per_sandwich = 2
    total_slices = sandwiches_eaten_Saturday * slices_per_sandwich + sandwiches_eaten_Sunday * slices_per_sandwich
    result = total_slices
    return result

print(solution())
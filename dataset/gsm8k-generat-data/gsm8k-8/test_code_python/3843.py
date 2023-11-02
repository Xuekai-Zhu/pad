def solution():
    total_slices = 8
    given_slices = ((1/2) + (1/2) + (1/4)) * total_slices
    remaining_slices = total_slices - given_slices
    result = remaining_slices
    return result

print(solution())
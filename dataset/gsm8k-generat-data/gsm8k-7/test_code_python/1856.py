def solution():
    # Danny's watermelons
    danny_num_watermelons = 3
    danny_slices_per_watermelon = 10
    total_danny_slices = danny_num_watermelons * danny_slices_per_watermelon

    # Sister's watermelons
    sister_num_watermelons = 1
    sister_slices_per_watermelon = 15
    total_sister_slices = sister_num_watermelons * sister_slices_per_watermelon

    # Total watermelon slices
    total_slices = total_danny_slices + total_sister_slices
    result = total_slices
    return result

print(solution())
def solution():
    
    large_apples = 3
    small_apples = 5
    slices_per_large_apple = 5
    slices_per_small_apple = 3
    total_slices = (large_apples * slices_per_large_apple) + (small_apples * slices_per_small_apple)
    slices_left = total_slices - 15
    result = slices_left
    return result

print(solution())
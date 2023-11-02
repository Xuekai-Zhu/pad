def solution():
    num_friends = 8
    slices_per_friend = 2
    slices_per_cake = 6
    num_cakes = 4
    num_slices_needed = num_friends * slices_per_friend
    num_slices_available = num_cakes * slices_per_cake
    num_slices_left_over = num_slices_available - num_slices_needed - 3
    result = num_slices_left_over
    return result

print(solution())
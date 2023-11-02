def solution():
    num_friends = 8
    num_slices_per_friend = 2
    num_slices_per_cake = 6
    num_cakes = 4
    num_slices_eaten_by_amber = 3

    # Calculate the total number of slices needed for all friends
    total_slices_needed = num_friends * num_slices_per_friend

    # Calculate the total number of slices that all cakes can provide
    total_slices_available = num_cakes * num_slices_per_cake

    # Calculate the total number of slices that will be left over
    total_slices_left = total_slices_available - total_slices_needed - num_slices_eaten_by_amber
    result = total_slices_left
    return result

print(solution())
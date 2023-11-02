def solution():
    # Calculate the total number of slices in both cakes
    total_slices = 2 * 8

    # Calculate the number of slices given away to friends
    friend_slices = total_slices // 4

    # Calculate the remaining number of slices after giving away some to friends
    remaining_slices_after_friends = total_slices - friend_slices

    # Calculate the number of slices given away to family
    family_slices = remaining_slices_after_friends // 3

    # Calculate the remaining number of slices after giving away some to family
    remaining_slices = remaining_slices_after_friends - family_slices - 3  # Alex eats 3 slices

    result = remaining_slices
    return result

print(solution())
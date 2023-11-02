def solution():
    # Define the initial number of slices
    total_slices = 2 * 8

    # Calculate the number of slices given away to friends
    friend_slices = total_slices / 4

    # Calculate the remaining slices after giving to friends
    remaining_slices = total_slices - friend_slices

    # Calculate the number of slices given away to family
    family_slices = remaining_slices / 3

    # Calculate the remaining slices after giving to family
    remaining_slices -= family_slices

    # Subtract the slices that Alex ate
    remaining_slices -= 3

    result = remaining_slices
    return result

print(solution())
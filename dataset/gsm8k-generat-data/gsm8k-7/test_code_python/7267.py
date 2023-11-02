def solution():
    num_slices = 8
    friend_slices = 2

    # Calculate the number of remaining slices after the friend eats 2 slices
    remaining_slices = num_slices - friend_slices

    # Calculate the number of slices James eats, which is half of the remaining slices
    james_slices = remaining_slices / 2
    result = james_slices
    return result

print(solution())
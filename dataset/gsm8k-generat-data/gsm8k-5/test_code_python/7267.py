def solution():
    total_slices = 8 * 2  # James orders an 8 piece pizza, each piece is cut into 2 slices
    friend_slices = 2  # James's friend eats 2 slices
    remaining_slices = total_slices - friend_slices  # James subtracts the slices his friend ate from the total
    james_slices = remaining_slices / 2  # James eats half of the remaining slices

    result = james_slices
    return result

print(solution())
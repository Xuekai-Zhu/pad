def solution():
    toby_rotations = 5 * 80  # Toby rotates 5 baseballs with 80 rotations each
    friend_rotations = 4 * 101  # Toby's friend rotates 4 apples with 101 rotations each

    # Calculate the total number of rotations made by the winner
    total_rotations = max(toby_rotations, friend_rotations)
    result = total_rotations
    return result

print(solution())
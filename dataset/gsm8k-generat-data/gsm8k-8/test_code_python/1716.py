def solution():
    # Calculate the total number of rotations Toby can make
    toby_rotations = 5 * 80

    # Calculate the total number of rotations Toby's friend can make
    friend_rotations = 4 * 101

    # Determine the winner based on total number of rotations
    if toby_rotations > friend_rotations:
        winner_rotations = toby_rotations
    else:
        winner_rotations = friend_rotations

    result = winner_rotations
    return result

print(solution())
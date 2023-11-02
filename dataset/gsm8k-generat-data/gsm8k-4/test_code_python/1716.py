def solution():
    """Toby is in a juggling contest with a friend. The winner is whoever gets the most objects rotated around in 4 minutes. Toby has 5 baseballs and each one makes 80 rotations. His friend has 4 apples and each one makes 101 rotations. How many total rotations of objects are made by the winner?"""
    # Calculate the total rotations Toby can make
    toby_rotations = 5 * 80

    # Calculate the total rotations his friend can make
    friend_rotations = 4 * 101

    # Determine who made the most rotations
    if toby_rotations > friend_rotations:
        winner_rotations = toby_rotations
    else:
        winner_rotations = friend_rotations

    # return the result
    result = winner_rotations
    return result

print(solution())
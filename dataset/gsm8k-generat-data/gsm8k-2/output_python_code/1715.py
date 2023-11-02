def solution():
    """Toby is in a juggling contest with a friend. The winner is whoever gets the most objects rotated around in 4 minutes. Toby has 5 baseballs and each one makes 80 rotations. His friend has 4 apples and each one makes 101 rotations. How many total rotations of objects are made by the winner?"""
    toby_rotations = 5 * 80
    friend_rotations = 4 * 101
    total_rotations = max(toby_rotations, friend_rotations)
    result = total_rotations
    return result

print(solution())
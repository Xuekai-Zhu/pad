def solution():
    """Toby is in a juggling contest with a friend. The winner is whoever gets the most objects rotated around in 4 minutes. Toby has 5 baseballs and each one makes 80 rotations. His friend has 4 apples and each one makes 101 rotations. How many total rotations of objects are made by the winner?"""
    # Define the number of objects and rotations for Toby and his friend
    TOBY_OBJECTS = 5
    TOBY_ROTATIONS = 80
    FRIEND_OBJECTS = 4
    FRIEND_ROTATIONS = 101

    # Calculate the total rotations for Toby and his friend
    toby_total = TOBY_OBJECTS * TOBY_ROTATIONS
    friend_total = FRIEND_OBJECTS * FRIEND_ROTATIONS

    # Determine who has the most rotations and display the total
    if toby_total > friend_total:
        result = toby_total
    else:
        result = friend_total
    return result

print(solution())
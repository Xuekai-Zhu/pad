def solution():
    """Toby is in a juggling contest with a friend. The winner is whoever gets the most objects rotated around in 4 minutes.
    Toby has 5 baseballs and each one makes 80 rotations. His friend has 4 apples and each one makes 101 rotations.
    How many total rotations of objects are made by the winner?"""
    toby_balls = 5
    toby_rotations_per_ball = 80
    toby_total_rotations = toby_balls * toby_rotations_per_ball
    
    friend_apples = 4
    friend_rotations_per_apple = 101
    friend_total_rotations = friend_apples * friend_rotations_per_apple
    
    total_rotations = max(toby_total_rotations, friend_total_rotations)
    result = total_rotations
    
    return result

print(solution())
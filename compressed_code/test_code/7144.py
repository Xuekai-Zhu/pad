def solution():
    
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
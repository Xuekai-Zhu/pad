def solution():
    
    small_ball_rubber = 50
    large_ball_rubber = 300
    pack_size = 5000
    small_balls_made = 22
    total_rubber_used = small_balls_made * small_ball_rubber
    remaining_rubber = pack_size - total_rubber_used
    large_balls_made = remaining_rubber // large_ball_rubber
    result = large_balls_made
    return result

print(solution())
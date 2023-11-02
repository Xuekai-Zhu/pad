def solution():
    
    bar_volume = 12 * 8 * 6
    num_bars = 10
    total_volume = bar_volume * num_bars
    ball_volume = 8
    num_balls = total_volume // ball_volume
    result = num_balls
    return result

print(solution())
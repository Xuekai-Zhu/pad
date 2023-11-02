def solution():
    
    bar_volume = 12 * 8 * 6
    ten_bars_volume = bar_volume * 10
    ball_volume = 8
    num_balls = ten_bars_volume // ball_volume
    result = num_balls
    return result

print(solution())
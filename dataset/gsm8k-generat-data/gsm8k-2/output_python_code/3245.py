def solution():
    """An iron bar measures 12 cm by 8 cm by 6 cm. A factory wants to melt ten iron bars and mold them into iron balls. Each iron ball has a volume of 8 cubic cm. How many iron balls have been molded?"""
    bar_volume = 12 * 8 * 6
    num_bars = 10
    total_volume = bar_volume * num_bars
    ball_volume = 8
    num_balls = total_volume // ball_volume
    result = num_balls
    return result

print(solution())
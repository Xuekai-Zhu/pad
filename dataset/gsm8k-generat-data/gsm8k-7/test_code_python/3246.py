def solution():
    iron_bar_length = 12
    iron_bar_width = 8
    iron_bar_height = 6

    iron_bar_volume = iron_bar_length * iron_bar_width * iron_bar_height

    num_iron_bars = 10
    total_iron_volume = iron_bar_volume * num_iron_bars

    ball_volume = 8
    num_balls = total_iron_volume // ball_volume
    result = num_balls
    return result

print(solution())
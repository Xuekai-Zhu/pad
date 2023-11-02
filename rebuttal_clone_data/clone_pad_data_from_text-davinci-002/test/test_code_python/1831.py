def solution():
    iron_bar_length = 12
    iron_bar_width = 8
    iron_bar_height = 6
    iron_bar_volume = iron_bar_length * iron_bar_width * iron_bar_height
    iron_balls_volume = 8
    iron_balls_per_bar = iron_bar_volume / iron_balls_volume
    iron_bars = 10
    total_iron_balls = iron_bars * iron_balls_per_bar
    result = total_iron_balls
    return result

print(solution())
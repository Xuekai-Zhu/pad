def solution():
    total_balls = 360
    red_balls = total_balls / 4
    remaining_balls = total_balls - red_balls
    blue_balls = remaining_balls / 5
    neither_red_nor_blue = total_balls - red_balls - blue_balls
    result = neither_red_nor_blue
    return result

print(solution())
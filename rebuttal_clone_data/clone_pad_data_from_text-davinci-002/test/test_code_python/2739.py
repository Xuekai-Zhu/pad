def solution():
    total_balls = 360
    red_balls = total_balls / 4
    blue_balls = (total_balls - red_balls) / 5
    neither_red_nor_blue_balls = total_balls - red_balls - blue_balls
    result = neither_red_nor_blue_balls
    return result

print(solution())
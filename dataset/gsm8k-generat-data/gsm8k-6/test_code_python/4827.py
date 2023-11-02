def solution():
    # Find the number of red balls
    red_balls = 360/4

    # Find the number of remaining balls
    remaining_balls = 360 - red_balls

    # Find the number of blue balls
    blue_balls = remaining_balls/5

    # Find the number of balls that are neither red nor blue
    neither_red_nor_blue = 360 - red_balls - blue_balls

    result = neither_red_nor_blue
    return result

print(solution())
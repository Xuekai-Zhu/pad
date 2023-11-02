def solution():
    # Calculate the number of red balls
    red_balls = 360 * 0.25

    # Calculate the number of remaining balls
    remaining_balls = 360 - red_balls

    # Calculate the number of blue balls
    blue_balls = remaining_balls * 0.2

    # Calculate the number of balls that are neither red nor blue
    neither_red_nor_blue = 360 - red_balls - blue_balls

    result = neither_red_nor_blue
    return result

print(solution())
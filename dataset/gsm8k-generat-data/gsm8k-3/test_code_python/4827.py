def solution():
    """There are 360 balls in the ball pit. If a quarter of the balls in the ball pit are red and a fifth of the remaining balls are blue. How many of the balls are neither red nor blue?"""
    # Calculate the number of red balls
    red_balls = 360 // 4

    # Calculate the number of balls remaining after removing the red balls
    remaining_balls = 360 - red_balls

    # Calculate the number of blue balls from the remaining
    blue_balls = remaining_balls // 5

    # Calculate the number of balls that are neither red nor blue
    neither_red_nor_blue_balls = 360 - red_balls - blue_balls

    # Display the number of balls that are neither red nor blue
    result = neither_red_nor_blue_balls
    return result

print(solution())
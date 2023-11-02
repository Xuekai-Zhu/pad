def solution():
    """There are 360 balls in the ball pit. If a quarter of the balls in the ball pit are red and a fifth of the remaining balls are blue. How many of the balls are neither red nor blue?"""
    # Define the total number of balls
    total_balls = 360

    # Calculate the number of red balls
    red_balls = total_balls // 4

    # Calculate the number of remaining balls
    remaining_balls = total_balls - red_balls

    # Calculate the number of blue balls
    blue_balls = remaining_balls // 5

    # Calculate the number of balls that are neither red nor blue
    neither_balls = total_balls - red_balls - blue_balls

    # return the result
    result = neither_balls
    return result

print(solution())
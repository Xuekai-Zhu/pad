def solution():
    # Calculate the number of pink balls and orange balls
    red_balls = 20
    blue_balls = 10
    pink_balls = 3 * orange_balls
    total_balls = 50

    # Calculate the number of orange balls
    orange_balls = (total_balls - red_balls - blue_balls) / 4

    result = orange_balls
    return result

print(solution())
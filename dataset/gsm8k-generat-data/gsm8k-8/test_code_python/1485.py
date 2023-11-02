def solution():
    # Define the number of red and blue balls
    red_balls = 20
    blue_balls = 10

    # Calculate the number of pink balls
    pink_balls = 3 * red_balls

    # Calculate the number of orange balls
    orange_balls = 50 - red_balls - blue_balls - pink_balls
    result = orange_balls
    return result

print(solution())
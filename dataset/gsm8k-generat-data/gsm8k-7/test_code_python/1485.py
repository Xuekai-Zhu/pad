def solution():
    total_balls = 50
    red_balls = 20
    blue_balls = 10

    # Calculate the number of pink and orange balls combined
    pink_orange_balls = total_balls - red_balls - blue_balls

    # Calculate the number of orange balls
    orange_balls = pink_orange_balls / 4

    result = orange_balls
    return result

print(solution())
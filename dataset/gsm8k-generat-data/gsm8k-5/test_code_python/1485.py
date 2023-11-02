def solution():
    total_balls = 50  # Adam has 50 balls in total
    red_balls = 20
    blue_balls = 10
    pink_orange_balls = total_balls - red_balls - blue_balls

    # Let the number of orange balls be x
    # Then the number of pink balls is 3x
    # And we know that pink_orange_balls = x + 3x = 4x
    # So x = pink_orange_balls / 4
    orange_balls = pink_orange_balls / 4
    result = orange_balls
    return result

print(solution())
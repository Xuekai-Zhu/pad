def solution():
    # Initial number of red balls
    red_balls = 16

    # Number of blue balls is twice the number of red balls
    blue_balls = 2 * red_balls

    # Jamie lost 6 of the red balls
    red_balls -= 6

    # Total number of balls remaining
    total_balls = 74

    # Calculate the number of blue balls remaining
    blue_balls = total_balls - red_balls

    # Calculate the number of yellow balls Jamie bought
    yellow_balls = blue_balls - 2 * red_balls

    result = yellow_balls
    return result

print(solution())
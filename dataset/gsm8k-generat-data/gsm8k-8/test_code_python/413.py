def solution():
    # Define the number of blue balls
    blue_balls = 11

    # Calculate the number of red balls
    red_balls = 2 * blue_balls

    # Calculate the total number of blue and red balls
    blue_red_total = blue_balls + red_balls

    # Calculate the number of green balls
    green_balls = 40 - blue_red_total

    result = green_balls
    return result

print(solution())
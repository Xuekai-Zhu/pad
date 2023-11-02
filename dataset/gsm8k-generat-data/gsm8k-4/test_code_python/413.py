def solution():
    """Ryan has 40 balls. There are twice as many red balls as blue while the rest are green. If there are 11 blue balls, how many green balls are there?"""
    # Define the total number of balls and the number of blue balls
    total_balls = 40
    blue_balls = 11

    # Calculate the number of red balls
    red_balls = blue_balls * 2

    # Calculate the number of green balls
    green_balls = total_balls - blue_balls - red_balls

    # Return the result
    result = green_balls
    return result

print(solution())
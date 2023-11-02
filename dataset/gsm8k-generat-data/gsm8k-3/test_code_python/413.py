def solution():
    """Ryan has 40 balls. There are twice as many red balls as blue while the rest are green. If there are 11 blue balls, how many green balls are there?"""
    # Define the number of blue and red balls
    blue_balls = 11
    red_balls = blue_balls * 2

    # Calculate the number of green balls
    green_balls = 40 - blue_balls - red_balls

    # Display the number of green balls
    result = green_balls
    return result

print(solution())
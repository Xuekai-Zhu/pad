def solution():
    # Calculate the number of red balls and green balls
    blue_balls = 11
    red_balls = 2 * blue_balls
    green_balls = 40 - blue_balls - red_balls  # the rest of the balls are green
    
    result = green_balls
    return result

print(solution())
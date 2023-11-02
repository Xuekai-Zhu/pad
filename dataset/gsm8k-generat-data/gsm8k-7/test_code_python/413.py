def solution():
    total_balls = 40
    num_blue_balls = 11
    num_red_balls = num_blue_balls * 2

    # Calculate the total number of blue and red balls
    total_blue_red_balls = num_blue_balls + num_red_balls

    # Calculate the total number of green balls
    total_green_balls = total_balls - total_blue_red_balls
    result = total_green_balls
    return result

print(solution())
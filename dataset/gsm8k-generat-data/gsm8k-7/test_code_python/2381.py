def solution():
    num_blue_balls = 6
    num_red_balls = 4
    num_green_balls = num_blue_balls * 3
    num_yellow_balls = num_red_balls * 2

    # Calculate the total number of balls in the box
    total_balls = num_blue_balls + num_red_balls + num_green_balls + num_yellow_balls
    result = total_balls
    return result

print(solution())
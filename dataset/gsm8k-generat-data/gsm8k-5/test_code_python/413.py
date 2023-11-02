def solution():
    blue_balls = 11  # There are 11 blue balls
    red_balls = 2 * blue_balls  # red balls are twice as many as blue balls
    total_red_blue_balls = blue_balls + red_balls  # red and blue balls combined
    green_balls = 40 - total_red_blue_balls  # remaining balls are green
    result = green_balls
    return result

print(solution())
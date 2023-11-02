def solution():
    initial_red_balls = 16
    initial_blue_balls = 2 * initial_red_balls
    balls_lost = 6
    final_red_balls = initial_red_balls - balls_lost
    final_blue_balls = initial_blue_balls
    total_balls = final_red_balls + final_blue_balls
    yellow_balls_bought = total_balls - (initial_red_balls + initial_blue_balls)
    result = yellow_balls_bought
    return result

print(solution())
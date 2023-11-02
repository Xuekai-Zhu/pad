def solution():
    """Jamie collects glass balls. He had 16 red balls and 2 times more blue balls. Later on, he lost 6 of the red balls, so he decided to buy some yellow balls to fill up his collection. How many yellow balls did he buy if, after all, he had 74 balls in total?"""
    red_balls_initial = 16
    blue_balls_initial = 2 * red_balls_initial
    total_initial = red_balls_initial + blue_balls_initial
    red_balls_final = red_balls_initial - 6
    total_final = 74
    yellow_balls = total_final - (red_balls_final + blue_balls_initial)
    result = yellow_balls
    return result

print(solution())
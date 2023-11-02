def solution():
    """Jamie collects glass balls. He had 16 red balls and two times more blue balls. Later on, he lost 6 of the red balls, so he decided to buy some yellow balls to fill up his collection. How many yellow balls did he buy if, after all, he had 74 balls in total?"""
    red_balls = 16
    blue_balls = 2 * red_balls
    total_balls = red_balls + blue_balls - 6  # subtract the lost red balls
    yellow_balls = 74 - total_balls
    result = yellow_balls
    return result

print(solution())
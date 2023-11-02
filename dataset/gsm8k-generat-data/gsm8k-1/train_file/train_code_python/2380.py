def solution():
    """Clive opens a box full of different colored balls. The box contains 6 blue balls, 4 red balls, 3 times as many green balls as blue ones and twice as many yellow ones as red ones. How many balls are in the box Clive opens?"""
    blue_balls = 6
    red_balls = 4
    green_balls = blue_balls * 3
    yellow_balls = red_balls * 2
    total_balls = blue_balls + red_balls + green_balls + yellow_balls
    result = total_balls
    return result

print(solution())
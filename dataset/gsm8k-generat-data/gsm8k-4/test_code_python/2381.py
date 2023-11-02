def solution():
    """Clive opens a box full of different colored balls. The box contains 6 blue balls, 4 red balls, 3 times as many green balls as blue ones and twice as many yellow ones as red ones. How many balls are in the box Clive opens? """
    # Define the number of blue and red balls
    blue_balls = 6
    red_balls = 4

    # Calculate the number of green and yellow balls
    green_balls = 3 * blue_balls
    yellow_balls = 2 * red_balls

    # Calculate the total number of balls
    total_balls = blue_balls + red_balls + green_balls + yellow_balls

    # return the result
    result = total_balls
    return result

print(solution())
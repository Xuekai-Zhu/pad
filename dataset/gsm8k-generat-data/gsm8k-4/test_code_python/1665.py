def solution():
    """Jamie collects glass balls. He had 16 red balls and two times more blue balls. Later on, he lost 6 of the red balls, so he decided to buy some yellow balls to fill up his collection. How many yellow balls did he buy if, after all, he had 74 balls in total?"""
    # Define the initial number of red balls
    red_balls = 16

    # Calculate the number of blue balls (2 times more than red balls)
    blue_balls = red_balls * 2

    # Calculate the initial number of balls
    initial_balls = red_balls + blue_balls

    # Calculate the number of remaining red balls after losing 6
    remaining_red_balls = red_balls - 6

    # Calculate the number of yellow balls needed to have a total of 74 balls
    yellow_balls = 74 - (remaining_red_balls + blue_balls)

    # return the result
    result = yellow_balls
    return result

print(solution())
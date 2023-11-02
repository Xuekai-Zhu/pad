def solution():
    """Jamie collects glass balls. He had 16 red balls and two times more blue balls. Later on, he lost 6 of the red balls, so he decided to buy some yellow balls to fill up his collection. How many yellow balls did he buy if, after all, he had 74 balls in total?"""
    # Calculate the number of blue balls
    blue_balls = 2 * 16

    # Calculate the number of total balls before losing six red balls
    total_balls_before_loss = 16 + blue_balls

    # Calculate the number of total balls after losing six red balls
    total_balls_after_loss = total_balls_before_loss - 6

    # Calculate the number of yellow balls bought
    yellow_balls = 74 - total_balls_after_loss

    # Display the number of yellow balls bought
    result = yellow_balls
    return result

print(solution())
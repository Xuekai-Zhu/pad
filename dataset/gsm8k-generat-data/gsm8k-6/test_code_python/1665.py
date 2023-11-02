def solution():
    # Calculate the number of blue balls
    blue_balls = 2 * 16

    # Calculate the total number of balls before losing the 6 red ones
    total_balls_before_loss = 16 + blue_balls

    # Calculate the total number of balls after losing the 6 red ones
    total_balls_after_loss = total_balls_before_loss - 6

    # Calculate the number of yellow balls needed to reach a total of 74 balls
    yellow_balls = 74 - total_balls_after_loss

    result = yellow_balls
    return result

print(solution())
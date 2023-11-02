def solution():
    # Calculate the number of blue balls
    blue_balls = 2 * 16

    # Calculate how many balls Jamie had before losing the 6 red balls
    total_before_loss = 16 + blue_balls

    # Calculate how many balls Jamie had after losing the 6 red balls
    total_after_loss = total_before_loss - 6

    # Calculate how many yellow balls Jamie bought
    yellow_balls = 74 - total_after_loss

    result = yellow_balls
    return result

print(solution())
def solution():
    num_yellow_balls = 27
    num_brown_balls = 33

    # Calculate the total number of balls that Veronica carried
    total_balls = num_yellow_balls + num_brown_balls

    # Calculate the percentage of balls that were yellow
    percentage_yellow = (num_yellow_balls / total_balls) * 100
    result = percentage_yellow
    return result

print(solution())
def solution():
    # Calculate the total steps taken so far
    total_steps = 9400 + 9100 + 8300 + 9200 + 8900

    # Calculate the number of steps Toby needs to reach his goal
    goal_steps = 9000 * 7 - total_steps

    # Calculate the average number of steps Toby needs to take on Friday and Saturday
    avg_steps = goal_steps / 2
    result = avg_steps
    return result

print(solution())
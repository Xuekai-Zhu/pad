def solution():
    # Calculate the total steps taken so far
    total_steps = 9400 + 9100 + 8300 + 9200 + 8900

    # Calculate the total steps needed for the whole week
    total_steps_needed = 7 * 9000

    # Calculate the steps needed for Friday and Saturday
    steps_needed = total_steps_needed - total_steps

    # Calculate the average steps needed per day for Friday and Saturday
    average_steps_needed = steps_needed / 2
    result = average_steps_needed
    return result

print(solution())
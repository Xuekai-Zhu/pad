def solution():
    # Find the total completion time for all four runners
    total_completion_time = 4 * 30  # average completion time of all four runners was 30 seconds

    # Find the total completion time for the last three runners
    last_three_completion_time = 3 * 35  # average completion time of the last three runners was 35 seconds

    # Find the completion time for the first runner
    first_runner_completion_time = total_completion_time - last_three_completion_time

    result = first_runner_completion_time
    return result

print(solution())
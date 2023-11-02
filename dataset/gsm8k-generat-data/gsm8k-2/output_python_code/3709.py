def solution():
    """4 students participated in a 200m race. If the average completion time of the last three students was 35 seconds, and the average completion time of all four runners was 30 seconds, how long (in seconds) did it take the student who came first to finish the race?"""
    total_time = 4 * 30 # total time for all four runners
    last_three_time = 3 * 35 # total time for last three runners
    first_runner_time = total_time - last_three_time # time for first runner
    result = first_runner_time
    return result

print(solution())
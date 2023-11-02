def solution():
    num_fast_runners = 5
    fast_runner_time = 8
    slow_runner_time = 10

    # Calculate the total time taken by the first five runners
    total_fast_runner_time = num_fast_runners * fast_runner_time

    # Calculate the total time taken by the last three runners
    total_slow_runner_time = 3 * slow_runner_time

    # Calculate the total time taken by all eight runners
    total_time = total_fast_runner_time + total_slow_runner_time
    result = total_time
    return result

print(solution())
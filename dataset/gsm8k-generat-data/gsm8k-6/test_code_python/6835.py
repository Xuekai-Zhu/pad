def solution():
    num_ski_runs = 0
    time_per_run = 15 + 5  # time in minutes for a complete ski run
    total_time = 120  # time in minutes for 2 hours
    while (total_time >= time_per_run):
        num_ski_runs += 1
        total_time -= time_per_run
    result = num_ski_runs
    return result

print(solution())
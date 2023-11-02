def solution():
    trumpet_time = 40  # Kenny practiced on the trumpet for 40 hours
    trumpet_to_run_ratio = 2  # Kenny practiced on the trumpet for twice as long as he ran
    run_time = trumpet_time / trumpet_to_run_ratio  # Calculate how long Kenny ran
    basketball_to_run_ratio = 0.5  # Kenny ran for twice as long as he played basketball
    basketball_time = run_time * basketball_to_run_ratio  # Calculate how long Kenny played basketball

    result = basketball_time
    return result

print(solution())
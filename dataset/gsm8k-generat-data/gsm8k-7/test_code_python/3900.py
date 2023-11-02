def solution():
    num_workers_1 = 15
    num_days_1 = 6
    total_wages_1 = 9450

    num_workers_2 = 19
    num_days_2 = 5

    # Calculate the daily wages per worker
    daily_wages_per_worker = total_wages_1 / (num_workers_1 * num_days_1)

    # Calculate the total wages for the second group of workers
    total_wages_2 = num_workers_2 * num_days_2 * daily_wages_per_worker
    result = total_wages_2
    return result

print(solution())
def solution():
    """If the wages of 15 workers for 6 days is $9450. What would be the wages for 19 workers for 5 days?"""
    worker_days = 15 * 6
    wages = 9450
    wages_per_worker_per_day = wages / worker_days
    new_worker_days = 19 * 5
    new_wages = wages_per_worker_per_day * new_worker_days * 19
    result = new_wages
    return result

print(solution())
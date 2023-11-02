def solution():
    workers = 15
    days = 6
    total_wages = 9450
    new_workers = 19
    new_days = 5
    new_wages = (total_wages / workers) * new_workers * (new_days / days)
    result = new_wages
    return result

print(solution())
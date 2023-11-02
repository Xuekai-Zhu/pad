def solution():
    
    num_workers = 3
    chairs_per_worker_per_hour = 4
    chairs_per_6_hours = 1
    total_chairs = num_workers * chairs_per_worker_per_hour * 6 + chairs_per_6_hours
    result = total_chairs
    return result

print(solution())
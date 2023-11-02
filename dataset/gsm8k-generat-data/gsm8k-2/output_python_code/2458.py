def solution():
    """There are 3 workers producing chairs in a furniture factory.
    Each of them produces 4 chairs an hour.
    As a group, they produce an additional chair every 6 hours.
    In total, how many chairs have been produced after 6 hours?"""
    num_workers = 3
    chairs_per_worker_per_hour = 4
    chairs_per_6_hours = 1
    total_chairs = num_workers * chairs_per_worker_per_hour * 6 + chairs_per_6_hours
    result = total_chairs
    return result

print(solution())
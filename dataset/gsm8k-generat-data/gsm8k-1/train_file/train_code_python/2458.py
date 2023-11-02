def solution():
    """There are 3 workers producing chairs in a furniture factory. Each of them produces 4 chairs an hour. As a group, they produce an additional chair every 6 hours. In total, how many chairs have been produced after 6 hours?"""
    workers = 3
    chairs_per_hour = 4
    extra_chair_every = 6
    total_chairs = workers * chairs_per_hour * 6
    extra_chairs = 6 // extra_chair_every
    total_chairs += extra_chairs
    result = total_chairs
    return result

print(solution())
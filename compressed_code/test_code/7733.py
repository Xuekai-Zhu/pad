def solution():
    
    workers = 3
    chairs_per_hour = 4
    extra_chair_every = 6
    total_chairs = workers * chairs_per_hour * 6
    extra_chairs = 6 // extra_chair_every
    total_chairs += extra_chairs
    result = total_chairs
    return result

print(solution())
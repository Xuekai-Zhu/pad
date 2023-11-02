def solution():
    crows = 3
    worms = 30
    worms_per_crow = worms / crows
    new_crows = 5
    new_worms = new_crows * worms_per_crow
    new_time = 2
    new_worms_per_hour = new_worms * new_time
    result = new_worms_per_hour
    
    return result

print(solution())
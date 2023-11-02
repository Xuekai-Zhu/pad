def solution():
    pool_size = 120
    drain_speed = 30
    hose_speed = 20
    hours_elapsed = 3
    water_left = pool_size - (drain_speed * hours_elapsed) + (hose_speed * hours_elapsed)
    result = water_left
    
    return result

print(solution())
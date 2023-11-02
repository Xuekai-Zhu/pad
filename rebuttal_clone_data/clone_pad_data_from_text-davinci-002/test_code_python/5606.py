def solution():
    vacuum_time = 45
    dust_time = 60
    mop_time = 30
    brush_time = 5
    cats = 3
    total_time = vacuum_time + dust_time + mop_time + (cats * brush_time)
    free_time_left = 180 - total_time
    
    return free_time_left

print(solution())
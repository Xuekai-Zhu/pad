def solution():
    
    stairs_per_floor = 1
    floors = 20
    seconds_per_stair = 11
    total_seconds_running = seconds_per_stair * stairs_per_floor * floors
    seconds_left = 72 - (total_seconds_running - 165)
    result = seconds_left
    return result

print(solution())
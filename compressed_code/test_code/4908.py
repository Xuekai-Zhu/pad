def solution():
    
    rottweiler_time = 20
    border_collie_time = 10
    chihuahua_time = 45
    num_rotts = 6
    num_borders = 9
    num_chis = 1
    total_time = (rottweiler_time * num_rotts) + (border_collie_time * num_borders) + (chihuahua_time * num_chis)
    result = total_time
    return result

print(solution())
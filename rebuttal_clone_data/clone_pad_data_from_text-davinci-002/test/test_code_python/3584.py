def solution():
    time_rot = 20
    time_bor = 10
    time_chi = 45
    num_rot = 6
    num_bor = 9
    num_chi = 1
    total_time = (num_rot * time_rot) + (num_bor * time_bor) + (num_chi * time_chi)
    result = total_time
    return result

print(solution())
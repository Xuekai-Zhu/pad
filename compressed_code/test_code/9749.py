def solution():
    
    pool_radius = 12
    pool_volume = 15000
    hose1_rate = 2
    hose2_rate = 2
    hose3_rate = 3
    hose4_rate = 3
    total_rate = hose1_rate + hose2_rate + hose3_rate + hose4_rate
    total_rate_gpm = total_rate * 60
    time_hours = pool_volume / total_rate_gpm
    result = time_hours
    return result

print(solution())
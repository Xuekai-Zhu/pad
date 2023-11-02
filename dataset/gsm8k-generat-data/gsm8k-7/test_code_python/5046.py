def solution():
    pool_radius = 24 / 2
    pool_depth = 4
    pool_volume = (3.14 * pool_radius ** 2) * pool_depth

    hose1_rate = 2
    hose2_rate = 2
    hose3_rate = 3
    hose4_rate = 3

    total_hose_rate = hose1_rate + hose2_rate + hose3_rate + hose4_rate
    total_time = (pool_volume / total_hose_rate) * 60
    hours = total_time / 60

    result = hours
    return result

print(solution())
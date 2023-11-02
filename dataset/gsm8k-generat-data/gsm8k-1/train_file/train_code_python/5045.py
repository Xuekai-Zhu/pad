def solution():
    """Gentry assembled a new 24 foot round pool in her backyard. To fill the pool with water, she used four hoses. Two of the hoses each deliver water at a rate of 2 gallons per minute. The other two hoses each deliver water at a rate of 3 gallons per minute. With a volume of 15,000 gallons, how many hours will it take to fill the pool?"""
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
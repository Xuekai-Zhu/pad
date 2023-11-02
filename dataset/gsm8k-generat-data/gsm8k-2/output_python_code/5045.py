def solution():
    """Gentry assembled a new 24 foot round pool in her backyard. To fill the pool with water, she used four hoses. Two of the hoses each deliver water at a rate of 2 gallons per minute. The other two hoses each deliver water at a rate of 3 gallons per minute. With a volume of 15,000 gallons, how many hours will it take to fill the pool?"""
    pool_radius = 24 / 2
    pool_volume = 15000
    pool_height = pool_volume / (math.pi * (pool_radius ** 2))
    # calculate the total flow rate of all hoses
    flow_rate = 2 * 2 + 2 * 3
    # calculate the time to fill the pool
    time_to_fill = (pool_volume / flow_rate) / 60
    result = time_to_fill
    return result

print(solution())
def solution():
    """Jim is a maintenance worker at a pool. Every time someone jumps in the pool, they cause 400 ml of water to splash out and evaporate. Jim has to get everyone out of the pool, clean, and refill it when it gets below 80% full. If the pool holds 2000 L of water, how many times can people jump in the pool before Jim has to clean it?"""
    pool_capacity = 2000
    splash_volume = 0.4
    volume_lost_per_jump = splash_volume / 1000
    water_capacity = pool_capacity * 0.8
    jumps_allowed = int(water_capacity / volume_lost_per_jump)
    result = jumps_allowed
    return result

print(solution())
def solution():
    """Lydia has a small pool she uses to bathe her dogs. When full, the pool holds 60 gallons of water. She fills her pool using the garden hose, which provides water at the rate of 1.6 gallons per minute. Unfortunately, her pool has a small hole that leaks water at a rate of 0.1 gallons per minute. How long will it take for her to fill the pool, in minutes?"""
    pool_capacity = 60
    fill_rate = 1.6
    leak_rate = 0.1
    net_fill_rate = fill_rate - leak_rate
    time_to_fill = pool_capacity / net_fill_rate
    result = time_to_fill
    return result

print(solution())
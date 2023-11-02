def solution():
    """Lydia has a small pool she uses to bathe her dogs. When full, the pool holds 60 gallons of water. She fills her pool using the garden hose, which provides water at the rate of 1.6 gallons per minute. Unfortunately, her pool has a small hole that leaks water at a rate of 0.1 gallons per minute. How long will it take for her to fill the pool, in minutes?"""
    # Define the size of the pool and the flow rates
    pool_size = 60
    fill_rate = 1.6
    leak_rate = 0.1

    # Calculate the net flow rate of water into the pool
    net_flow_rate = fill_rate - leak_rate

    # Calculate the time it takes to fill the pool
    fill_time = pool_size / net_flow_rate

    result = fill_time
    return result

print(solution())
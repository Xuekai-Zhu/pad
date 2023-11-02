def solution():
    """Lydia has a small pool she uses to bathe her dogs.  When full, the pool holds 60 gallons of water.  She fills her pool using the garden hose, which provides water at the rate of 1.6 gallons per minute.  Unfortunately, her pool has a small hole that leaks water at a rate of 0.1 gallons per minute.  How long will it take for her to fill the pool, in minutes?"""
    # Define the pool capacity and fill rate
    POOL_CAPACITY = 60
    FILL_RATE = 1.6
    LEAK_RATE = 0.1

    # Calculate the net fill rate
    net_fill_rate = FILL_RATE - LEAK_RATE

    # Calculate the time to fill the pool
    time_to_fill = POOL_CAPACITY / net_fill_rate

    # Display the time to fill the pool
    result = time_to_fill
    return result

print(solution())
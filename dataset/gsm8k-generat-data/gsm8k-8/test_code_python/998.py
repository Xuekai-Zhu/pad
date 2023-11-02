def solution():
    # Define the pool capacity and the filling and leaking rates
    pool_capacity = 60
    filling_rate = 1.6
    leaking_rate = 0.1

    # Calculate the net filling rate
    net_filling_rate = filling_rate - leaking_rate

    # Calculate the time to fill the pool
    time_to_fill = pool_capacity / net_filling_rate
    result = time_to_fill
    return result

print(solution())
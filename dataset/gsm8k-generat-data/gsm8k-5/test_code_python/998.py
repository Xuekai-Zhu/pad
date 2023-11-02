def solution():
    pool_capacity = 60  # The pool can hold 60 gallons of water
    hose_rate = 1.6  # The hose fills the pool at a rate of 1.6 gallons per minute
    leak_rate = 0.1  # The pool leaks at a rate of 0.1 gallons per minute

    # Calculate the net fill rate of the pool
    net_fill_rate = hose_rate - leak_rate

    # Calculate how long it will take to fill the pool
    time_to_fill = pool_capacity / net_fill_rate
    result = time_to_fill
    return result

print(solution())
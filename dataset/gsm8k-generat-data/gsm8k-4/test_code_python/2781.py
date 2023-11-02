def solution():
    """When Patrick, Manu, and Amy participate in a race they realize that Patrick finishes the race in 60 seconds. Manu took 12 more seconds to finish the race. If Amy is twice as fast as Manu, how long did it take her to finish the race?"""
    # Define Patrick's time
    patrick_time = 60

    # Calculate Manu's time
    manu_time = patrick_time + 12

    # Calculate Amy's time
    amy_time = manu_time / 2

    # Return Amy's time
    result = amy_time
    return result

print(solution())
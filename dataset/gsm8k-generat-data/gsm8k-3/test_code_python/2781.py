def solution():
    """When Patrick, Manu, and Amy participate in a race they realize that Patrick finishes the race in 60 seconds. Manu took 12 more seconds to finish the race. If Amy is twice as fast as Manu, how long did it take her to finish the race?"""
    # Define Patrick's time as 60 seconds
    patrick_time = 60

    # Define Manu's time as 12 seconds more than Patrick's time
    manu_time = patrick_time + 12

    # Define Amy's speed as twice as fast as Manu's speed
    amy_speed = 2 * (1 / manu_time)

    # Calculate Amy's time using the formula: time = distance / speed
    # Assume the distance is the same for all three participants
    amy_time = (distance / amy_speed)

    # Display Amy's time
    result = amy_time
    return result

print(solution())
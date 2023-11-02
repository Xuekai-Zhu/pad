def solution():
    patrick_time = 60  # Patrick finishes the race in 60 seconds
    manu_time = patrick_time + 12  # Manu took 12 more seconds to finish the race
    amy_speed = 2  # Amy is twice as fast as Manu
    manu_speed = 1  # Let Manu's speed be 1, then Amy's speed is 2

    # Calculate the time it took Amy to finish the race
    amy_time = (patrick_time / manu_speed) / amy_speed

    result = amy_time
    return result

print(solution())
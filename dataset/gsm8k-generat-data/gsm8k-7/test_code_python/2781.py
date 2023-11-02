def solution():
    patrick_time = 60
    manu_time = patrick_time + 12
    amy_speed = 2/3   # If Manu took 72 seconds, then Amy took 36 seconds.

    # Calculate Amy's time based on her speed
    amy_time = (patrick_time + manu_time) / amy_speed

    result = amy_time
    return result

print(solution())
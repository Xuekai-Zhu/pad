def solution():
    omar_feet_per_minute = 240/12  # Omar can raise his kite at a rate of 20 feet per minute
    jasper_feet_per_minute = omar_feet_per_minute * 3  # Jasper can raise his kite at three times the rate Omar can

    # Calculate the time it will take for Jasper to raise his kite to a height of 600 feet
    time = 600 / jasper_feet_per_minute
    result = time
    return result

print(solution())
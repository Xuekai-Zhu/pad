def solution():
    # Calculate Omar's rate of raising his kite
    omar_rate = 240/12 # 20 feet per minute

    # Calculate Jasper's rate of raising his kite
    jasper_rate = omar_rate * 3 # 60 feet per minute

    # Calculate the time it will take for Jasper to raise his kite to 600 feet
    jasper_time = 600/jasper_rate # 10 minutes

    result = jasper_time
    return result

print(solution())
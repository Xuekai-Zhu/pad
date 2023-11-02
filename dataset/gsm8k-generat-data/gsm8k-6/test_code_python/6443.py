def solution():
    # Calculate the rate at which Omar raises his kite
    omar_rate = 240/12  # feet raised per minute

    # Calculate the time it takes for Jasper to raise his kite
    jasper_rate = 3 * omar_rate
    jasper_time = 600/jasper_rate  # time in minutes

    result = jasper_time
    return result

print(solution())
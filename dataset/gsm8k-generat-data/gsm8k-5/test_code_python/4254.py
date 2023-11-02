def solution():
    normal_temperature = 95  # Tony normally has a temperature of 95 degrees
    fever_threshold = 100  # A fever is anything over 100 degrees
    sickness_raise = 10  # The sickness raises his temperature by 10 degrees

    # Calculate Tony's temperature after the sickness
    new_temperature = normal_temperature + sickness_raise

    # Calculate how many degrees above the fever threshold his temperature is
    above_threshold = new_temperature - fever_threshold

    result = above_threshold
    return result

print(solution())
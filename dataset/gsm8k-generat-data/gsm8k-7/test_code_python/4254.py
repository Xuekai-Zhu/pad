def solution():
    normal_temp = 95
    sickness_temp_increase = 10
    fever_threshold = 100

    # Calculate Tony's temperature with the sickness
    sickness_temp = normal_temp + sickness_temp_increase

    # Calculate how many degrees above the fever threshold Tony's temperature is
    fever_temp_diff = sickness_temp - fever_threshold
    result = fever_temp_diff
    return result

print(solution())
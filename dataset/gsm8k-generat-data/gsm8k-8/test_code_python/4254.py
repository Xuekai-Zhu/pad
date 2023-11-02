def solution():
    # Define Tony's normal temperature and the increase from his sickness
    normal_temp = 95
    sickness_increase = 10

    # Calculate Tony's temperature after his sickness
    sick_temp = normal_temp + sickness_increase

    # Calculate how many degrees above the fever threshold his temperature is
    fever_threshold = 100
    above_fever_threshold = sick_temp - fever_threshold

    result = above_fever_threshold
    return result

print(solution())
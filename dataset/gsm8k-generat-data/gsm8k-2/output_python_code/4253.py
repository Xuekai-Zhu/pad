def solution():
    """If Tony normally has a temperature of 95 degrees, and he comes down with a sickness that raises his temperature by 10 degrees, how many degrees above the threshold of fever is his temperature if a fever is anything over 100 degrees?"""
    normal_temp = 95
    sickness_temp = 10
    new_temp = normal_temp + sickness_temp
    fever_threshold = 100
    above_fever_threshold = new_temp - fever_threshold
    result = above_fever_threshold
    return result

print(solution())
def solution():
    """If Tony normally has a temperature of 95 degrees, and he comes down with a sickness that raises his temperature by 10 degrees, how many degrees above the threshold of fever is his temperature if a fever is anything over 100 degrees?"""
    normal_temp = 95
    sick_temp = normal_temp + 10
    fever_threshold = 100
    degrees_above_fever = sick_temp - fever_threshold
    result = degrees_above_fever if degrees_above_fever > 0 else 0
    return result

print(solution())
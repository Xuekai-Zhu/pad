def solution():
    """If Tony normally has a temperature of 95 degrees, and he comes down with a sickness that raises his temperature by 10 degrees, how many degrees above the threshold of fever is his temperature if a fever is anything over 100 degrees?"""
    # Define Tony's normal temperature and the increase due to his illness
    normal_temp = 95
    illness_increase = 10

    # Calculate Tony's temperature with the illness
    illness_temp = normal_temp + illness_increase

    # Calculate how many degrees above the fever threshold his temperature is
    above_fever_threshold = illness_temp - 100

    result = above_fever_threshold
    return result

print(solution())
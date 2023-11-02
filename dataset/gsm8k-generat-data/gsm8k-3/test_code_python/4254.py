def solution():
    """If Tony normally has a temperature of 95 degrees, and he comes down with a sickness that raises his temperature by 10 degrees, how many degrees above the threshold of fever is his temperature if a fever is anything over 100 degrees?"""
    # Define Tony's normal temperature and the temperature threshold for a fever
    NORMAL_TEMP = 95
    FEVER_THRESHOLD = 100

    # Calculate Tony's temperature with the sickness
    tony_temp = NORMAL_TEMP + 10

    # Calculate how many degrees above the fever threshold Tony's temperature is
    fever_diff = tony_temp - FEVER_THRESHOLD

    # Display how many degrees above the fever threshold Tony's temperature is
    result = fever_diff
    return result

print(solution())
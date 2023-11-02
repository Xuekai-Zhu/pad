def solution():
    """Noah, who loves his Grammy, calls her every week to talk about his day. If each call lasts 30 minutes and he is charged $0.05 per call minute, how much would he be billed if he makes the calls for a year?"""
    # Define the minutes per week and weeks per year
    MINUTES_PER_WEEK = 30
    WEEKS_PER_YEAR = 52

    # Calculate the total minutes per year
    total_minutes = MINUTES_PER_WEEK * WEEKS_PER_YEAR

    # Calculate the total cost
    total_cost = total_minutes * 0.05

    # return the result
    result = total_cost
    return result

print(solution())
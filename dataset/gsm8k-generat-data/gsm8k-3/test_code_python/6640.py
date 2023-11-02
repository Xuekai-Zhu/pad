def solution():
    """Noah, who loves his Grammy, calls her every week to talk about his day. If each call lasts 30 minutes and he is charged $0.05 per call minute, how much would he be billed if he makes the calls for a year?"""
    # Define the length of each call in minutes and the cost per minute
    CALL_LENGTH = 30
    COST_PER_MINUTE = 0.05

    # Calculate the total number of minutes Noah spends on the phone with Grammy in a year
    total_minutes = CALL_LENGTH * 52

    # Calculate the total cost of the calls
    total_cost = total_minutes * COST_PER_MINUTE

    # Display the total cost
    result = total_cost
    return result

print(solution())
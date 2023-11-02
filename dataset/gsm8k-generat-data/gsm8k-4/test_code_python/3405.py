def solution():
    """James hires a seamstress to fix all his shirts and pants. He has 10 shirts and 12 pairs of pants. It takes 1.5 hours to fix a shirt and twice as long for pants. The tailor charges $30 per hour. How much does it cost?"""
    # Define the number of shirts and pants
    num_shirts = 10
    num_pants = 12

    # Define the time to fix a shirt and pants
    time_shirt = 1.5
    time_pants = 3.0

    # Define the cost per hour
    cost_hour = 30.0

    # Calculate the total time to fix all shirts and pants
    total_time = num_shirts * time_shirt + num_pants * time_pants

    # Calculate the total cost
    total_cost = total_time * cost_hour

    # return the result
    result = total_cost
    return result

print(solution())
def solution():
    """James hires a seamstress to fix all his shirts and pants.  He has 10 shirts and 12 pairs of pants.  It takes 1.5 hours to fix a shirt and twice as long for pants.  The tailor charges $30 per hour.  How much does it cost?"""
    # Define the number of shirts and pants
    num_shirts = 10
    num_pants = 12

    # Define the time taken to fix a shirt and a pair of pants
    shirt_time = 1.5
    pant_time = 2 * shirt_time

    # Calculate the total time taken to fix all the shirts and pants
    total_time = num_shirts * shirt_time + num_pants * pant_time

    # Calculate the total cost
    hourly_rate = 30
    total_cost = total_time * hourly_rate

    # Display the total cost
    result = total_cost
    return result

print(solution())
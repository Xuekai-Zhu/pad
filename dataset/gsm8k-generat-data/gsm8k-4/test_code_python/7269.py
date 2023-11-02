def solution():
    """Stan hires a magician for $60 an hour. He works 3 hours every day for 2 weeks. How much money does he pay the magician?"""
    # Define the hourly rate and the number of days
    HOURLY_RATE = 60
    NUM_DAYS = 14

    # Calculate the total number of hours worked by the magician
    total_hours = 3 * NUM_DAYS

    # Calculate the total cost of hiring the magician
    total_cost = total_hours * HOURLY_RATE

    # return the result
    result = total_cost
    return result

print(solution())
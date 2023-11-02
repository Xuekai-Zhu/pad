def solution():
    """Stan hires a magician for $60 an hour.  He works 3 hours every day for 2 weeks. How much money does he pay the magician?"""
    # Define the hourly rate and number of hours worked per day
    HOURLY_RATE = 60
    HOURS_PER_DAY = 3

    # Calculate the number of hours worked over 2 weeks
    hours_worked = HOURS_PER_DAY * 14

    # Calculate the total cost of hiring the magician
    total_cost = hours_worked * HOURLY_RATE

    # Display the total cost
    result = total_cost
    return result

print(solution())
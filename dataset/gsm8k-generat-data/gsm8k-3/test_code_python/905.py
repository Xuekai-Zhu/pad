def solution():
    """Sue works in a factory and every 30 minutes, a machine she oversees produces 30 cans of soda. How many cans of soda can one machine produce in 8 hours?"""
    # Define the number of minutes in 8 hours and the number of cans produced in 30 minutes
    MINUTES_IN_HOUR = 60
    CANS_PER_30_MINUTES = 30

    # Calculate the number of cans produced in 8 hours
    cans_per_hour = CANS_PER_30_MINUTES * 2 # since there are 2 30-minute intervals in an hour
    cans_per_day = cans_per_hour * MINUTES_IN_HOUR * 8 # since there are 8 hours in a day

    # Display the number of cans produced in 8 hours
    result = cans_per_day
    return result

print(solution())
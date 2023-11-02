def solution():
    """Bob can shuck 10 oysters in 5 minutes. How many oysters can he shuck in 2 hours?"""
    # Define the number of oysters Bob can shuck per minute
    oysters_per_minute = 2

    # Define the number of minutes in 2 hours
    minutes = 120

    # Calculate the total number of oysters Bob can shuck in 2 hours
    total_oysters = oysters_per_minute * minutes

    # Return the result
    result = total_oysters
    return result

print(solution())
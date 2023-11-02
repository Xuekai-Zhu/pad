def solution():
    """Bob can shuck 10 oysters in 5 minutes.  How many oysters can he shuck in 2 hours?"""
    # Convert 2 hours to minutes
    time_in_minutes = 2 * 60

    # Calculate the number of oysters Bob can shuck in 1 minute
    oysters_per_minute = 10 / 5

    # Calculate the total number of oysters Bob can shuck in 2 hours
    total_oysters = oysters_per_minute * time_in_minutes

    result = total_oysters
    return result

print(solution())
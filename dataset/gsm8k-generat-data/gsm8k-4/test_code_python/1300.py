def solution():
    """Martin spends 2 hours waiting in traffic, then four times that long trying to get off the freeway. How much time does he waste total?"""
    # Define the time Martin spends waiting in traffic
    waiting_time = 2

    # Calculate the time Martin spends trying to get off the freeway
    exiting_time = waiting_time * 4

    # Calculate the total time Martin wastes
    total_time = waiting_time + exiting_time

    # Return the result
    result = total_time
    return result

print(solution())
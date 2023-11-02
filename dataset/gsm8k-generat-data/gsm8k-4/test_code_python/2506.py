def solution():
    """Tom has only been getting 6 hours of sleep a day. He increases that by 1/3. How many hours of sleep does he get per night?"""
    # Define Tom's initial sleep time
    initial_sleep = 6

    # Calculate the increase in sleep time
    increase = initial_sleep * (1/3)

    # Calculate Tom's total sleep time after the increase
    total_sleep = initial_sleep + increase

    # Display the result
    result = total_sleep
    return result

print(solution())
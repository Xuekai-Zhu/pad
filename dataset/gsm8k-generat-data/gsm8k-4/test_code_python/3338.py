def solution():
    """Nicky went to the DMV. He spent 20 minutes waiting to take a number, and quadruple that amount of time plus 14 minutes waiting for his number to be called. How long did he wait total?"""
    # Define the time spent waiting to take a number in minutes
    wait_to_take_number = 20

    # Define the time spent waiting for the number to be called in minutes
    wait_for_number = wait_to_take_number * 4 + 14
    
    # Calculate the total time spent waiting in minutes
    total_wait_time = wait_to_take_number + wait_for_number

    # return the result in minutes
    result = total_wait_time
    return result

print(solution())
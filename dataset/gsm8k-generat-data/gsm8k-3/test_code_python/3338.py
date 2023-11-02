def solution():
    """Nicky went to the DMV. He spent 20 minutes waiting to take a number, and quadruple that amount of time plus 14 minutes waiting for his number to be called. How long did he wait total?"""
    # Define the time spent waiting to take a number and the time spent waiting for his number to be called
    wait_for_number = 20
    wait_for_call = 4 * wait_for_number + 14

    # Calculate the total time Nicky waited
    total_wait = wait_for_number + wait_for_call

    # Display the total time Nicky waited
    result = total_wait
    return result

print(solution())
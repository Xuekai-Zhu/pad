def solution():
    """Nicky went to the DMV. He spent 20 minutes waiting to take a number, and quadruple that amount of time plus 14 minutes waiting for his number to be called.
    How long did he wait total?"""
    time_waiting_for_number = 4 * 20 + 14 # Quadruple the time spent taking a number and add 14 minutes waiting for his number to be called
    total_time_waiting = 20 + time_waiting_for_number # Add the time spent taking a number to the time waiting for his number to be called
    result = total_time_waiting
    return result

print(solution())
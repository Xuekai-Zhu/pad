def solution():
    """Nicky went to the DMV. He spent 20 minutes waiting to take a number, and quadruple that amount of time plus 14 minutes waiting for his number to be called. How long did he wait total?"""
    take_number_time = 20
    call_number_time = take_number_time * 4 + 14
    total_time = take_number_time + call_number_time
    result = total_time
    return result

print(solution())
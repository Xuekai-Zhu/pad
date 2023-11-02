def solution():
    """Martin spends 2 hours waiting in traffic, then four times that long trying to get off the freeway. How much time does he waste total?"""
    time_waiting = 2
    time_getting_off = 4 * time_waiting
    total_time_wasted = time_waiting + time_getting_off
    result = total_time_wasted
    return result

print(solution())
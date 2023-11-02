def solution():
    """Martin spends 2 hours waiting in traffic, then four times that long trying to get off the freeway. How much time does he waste total?"""
    traffic_wait_time = 2
    freeway_exit_time = 4 * traffic_wait_time
    total_wasted_time = traffic_wait_time + freeway_exit_time
    result = total_wasted_time
    return result

print(solution())
def solution():
    # Define the time spent waiting in traffic and getting off the freeway
    traffic_wait = 2
    freeway_time = 4 * traffic_wait

    # Calculate the total wasted time
    total_wasted_time = traffic_wait + freeway_time
    result = total_wasted_time
    return result

print(solution())
def solution():
    # Define time spent turning off and on the router
    router_time = 10 * 6

    # Define time spent on hold with Comcast
    comcast_time = 6 * 10

    # Define time spent yelling at customer service representative
    yelling_time = 0.5 * comcast_time

    # Calculate total time spent
    total_time = router_time + comcast_time + yelling_time
    result = total_time
    return result

print(solution())
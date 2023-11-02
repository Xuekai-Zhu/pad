def solution():
    router_time = 10  # Martha spends 10 minutes turning the router off and on
    comcast_time = 6 * 10  # Martha spends 6 times 10 minutes on hold with Comcast
    yelling_time = comcast_time / 2  # Martha spends half as much time yelling at a customer service representative as she did on hold

    # Calculate total time Martha spent on these activities
    total_time = router_time + comcast_time + yelling_time
    result = total_time
    return result

print(solution())
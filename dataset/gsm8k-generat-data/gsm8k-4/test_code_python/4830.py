def solution():
    """Martha spends 10 minutes turning the router off and on again, six times that long on hold with Comcast, and half as much time as she spent on hold yelling at a customer service representative. How much time did Martha spend on these activities total?"""
    # Define the time spent turning off and on the router
    router_time = 10

    # Define the time spent on hold with Comcast
    comcast_time = router_time * 6

    # Define the time spent yelling at a customer service representative
    yelling_time = comcast_time / 2

    # Calculate the total time spent on these activities
    total_time = router_time + comcast_time + yelling_time

    result = total_time
    return result

print(solution())
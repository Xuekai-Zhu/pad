def solution():
    """Martha spends 10 minutes turning the router off and on again, six times that long on hold with Comcast, and half as much time as she spent on hold yelling at a customer service representative. How much time did Martha spend on these activities total?"""
    # Define the amount of time spent on each activity
    router_time = 10
    comcast_time = 6 * router_time
    yelling_time = comcast_time / 2

    # Calculate the total time spent
    total_time = router_time + comcast_time + yelling_time

    # Display the total time spent
    result = total_time
    return result

print(solution())
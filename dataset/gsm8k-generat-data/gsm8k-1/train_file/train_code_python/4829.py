def solution():
    """Martha spends 10 minutes turning the router off and on again, six times that long on hold with Comcast, and half as much time as she spent on hold yelling at a customer service representative. How much time did Martha spend on these activities total?"""
    router_time = 10
    hold_time = 6 * router_time
    yelling_time = hold_time / 2
    total_time = router_time + hold_time + yelling_time
    result = total_time
    return result

print(solution())
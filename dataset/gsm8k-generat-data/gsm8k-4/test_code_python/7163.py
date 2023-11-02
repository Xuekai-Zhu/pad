def solution():
    """Malcolm is trying to find the fastest walk to school and is currently comparing two routes. In the first route, he walks for 6 minutes uphill, walks for twice this amount of time along a path, then finishes the journey in a third of the time it took to walk the first two stages. In the second route, he walks along a flat path for 14 minutes, then finishes the walk in twice this amount of time. In minutes, how much longer was the second route compared with the first?"""
    # Calculate the time it takes for the first route
    stage1_time = 6
    stage2_time = stage1_time * 2
    stage3_time = (stage1_time + stage2_time) / 3
    first_route_time = stage1_time + stage2_time + stage3_time

    # Calculate the time it takes for the second route
    second_route_time = 14 + (2 * 14)

    # Calculate the difference in time between the two routes
    time_difference = second_route_time - first_route_time

    result = time_difference
    return result

print(solution())
def solution():
    """Malcolm is trying to find the fastest walk to school and is currently comparing two routes. In the first route, he walks for 6 minutes uphill, walks for twice this amount of time along a path, then finishes the journey in a third of the time it took to walk the first two stages. In the second route, he walks along a flat path for 14 minutes, then finishes the walk in twice this amount of time. In minutes, how much longer was the second route compared with the first?"""
    time_uphill = 6
    time_flat = 14
    time_rest_of_first_route = (time_uphill * 2) + (time_uphill / 3)
    time_second_route = (time_flat * 2) + time_flat
    difference_in_time = time_second_route - time_rest_of_first_route
    result = difference_in_time
    return result

print(solution())
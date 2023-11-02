def solution():
    """Malcolm is trying to find the fastest walk to school and is currently comparing two routes. In the first route, he walks for 6 minutes uphill, walks for twice this amount of time along a path, then finishes the journey in a third of the time it took to walk the first two stages. In the second route, he walks along a flat path for 14 minutes, then finishes the walk in twice this amount of time. In minutes, how much longer was the second route compared with the first?"""
    route1_time = 6 + (2 * 6) + (1/3 * (6 + (2 * 6)))
    route2_time = 14 + (2 * 14)
    time_diff = route2_time - route1_time
    result = time_diff
    return result

print(solution())
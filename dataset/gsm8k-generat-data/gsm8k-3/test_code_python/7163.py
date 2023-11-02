def solution():
    """Malcolm is trying to find the fastest walk to school and is currently comparing two routes. In the first route, he walks for 6 minutes uphill, walks for twice this amount of time along a path, then finishes the journey in a third of the time it took to walk the first two stages. In the second route, he walks along a flat path for 14 minutes, then finishes the walk in twice this amount of time. In minutes, how much longer was the second route compared with the first?"""
    # Calculate the time taken for the first route
    time_uphill = 6
    time_path = 2 * time_uphill
    time_finish = time_path / 3
    time_route1 = time_uphill + time_path + time_finish

    # Calculate the time taken for the second route
    time_flat = 14
    time_finish2 = 2 * time_flat
    time_route2 = time_flat + time_finish2

    # Calculate the difference in time between the two routes
    time_difference = time_route2 - time_route1

    # Display the difference in time
    result = time_difference
    return result

print(solution())
def solution():
    """Joseph wants to go to Boston for a road trip. If he takes route A, it will take him 5 hours to arrive; but if he takes route B, it will only take him 2 hours to arrive at his destination. How much time will he save if he takes route B to Boston and back to his home?"""
    # Calculate the time it takes to travel to Boston and back on route A
    routeA_time = 5 + 5

    # Calculate the time it takes to travel to Boston and back on route B
    routeB_time = 2 + 2

    # Calculate the time saved by taking route B
    time_saved = routeA_time - routeB_time

    # return the result
    result = time_saved
    return result

print(solution())
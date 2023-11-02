def solution():
    """Joseph wants to go to Boston for a road trip. If he takes route A, it will take him 5 hours to arrive; but if he takes route B, it will only take him 2 hours to arrive at his destination. How much time will he save if he takes route B to Boston and back to his home?"""
    time_route_a = 5
    time_route_b = 2
    time_saved = (time_route_a - time_route_b) * 2
    result = time_saved
    return result

print(solution())
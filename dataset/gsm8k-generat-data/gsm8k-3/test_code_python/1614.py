def solution():
    """Joseph wants to go to Boston for a road trip. If he takes route A, it will take him 5 hours to arrive; but if he takes route B, it will only take him 2 hours to arrive at his destination. How much time will he save if he takes route B to Boston and back to his home?"""
    # Define the time it takes for each route
    ROUTE_A_TIME = 5
    ROUTE_B_TIME = 2

    # Calculate the total time for round trip for both routes
    total_time_route_a = (ROUTE_A_TIME * 2)
    total_time_route_b = (ROUTE_B_TIME * 2)

    # Calculate the time saved by taking route B
    time_saved = total_time_route_a - total_time_route_b

    # Display the time saved
    result = time_saved
    return result

print(solution())
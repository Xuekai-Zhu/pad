def solution():
    """Patrick buys a season pass for each of his sons to visit the local amusement park as often as they want.  The passes were $100.00 each.  The oldest son went to the park 35 times over the summer and the youngest went 15 times.  What was the cost per trip to the park?"""
    # Define the cost of the season pass
    SEASON_PASS_COST = 100.00

    # Define the number of times each son went to the park
    oldest_son_trips = 35
    youngest_son_trips = 15

    # Calculate the total cost of both season passes
    total_cost = SEASON_PASS_COST * 2

    # Calculate the cost per trip to the park for both sons together
    cost_per_trip = total_cost / (oldest_son_trips + youngest_son_trips)

    # Display the cost per trip to the park
    result = cost_per_trip
    return result

print(solution())
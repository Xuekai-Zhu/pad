def solution():
    pass_price = 100.0
    oldest_visits = 35
    youngest_visits = 15

    # Calculate the total number of visits to the park by both sons
    total_visits = oldest_visits + youngest_visits

    # Calculate the total cost of both season passes
    total_cost = 2 * pass_price

    # Calculate the cost per trip to the park
    cost_per_trip = total_cost / total_visits
    result = cost_per_trip
    return result

print(solution())
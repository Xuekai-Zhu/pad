def solution():
    num_of_sons = 2  # Patrick has 2 sons with season passes
    cost_per_pass = 100  # Each pass costs $100
    oldest_son_visits = 35  # The oldest son goes to the park 35 times
    youngest_son_visits = 15  # The youngest son goes to the park 15 times

    # Calculate the total cost of the two season passes
    total_cost = num_of_sons * cost_per_pass

    # Calculate the total number of times the sons visited the park
    total_visits = oldest_son_visits + youngest_son_visits

    # Calculate the cost per trip to the park
    cost_per_trip = total_cost / total_visits
    result = cost_per_trip
    return result

print(solution())
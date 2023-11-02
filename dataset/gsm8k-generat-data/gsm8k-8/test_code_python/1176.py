def solution():
    # Define the number of times Paula wants to ride each ride
    go_karts_times = 1
    bumper_cars_times = 4

    # Define the cost of each ride in tickets
    go_karts_cost = 4
    bumper_cars_cost = 5

    # Calculate the total number of tickets Paula needs
    total_tickets = go_karts_times * go_karts_cost + bumper_cars_times * bumper_cars_cost
    result = total_tickets
    return result

print(solution())
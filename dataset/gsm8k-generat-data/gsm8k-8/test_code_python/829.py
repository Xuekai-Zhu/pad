def solution():
    # Define the ticket costs and Jeanne's current number of tickets
    ferris_wheel_cost = 5
    roller_coaster_cost = 4
    bumper_cars_cost = 4
    current_tickets = 5

    # Calculate the total cost of the rides Jeanne wants to go on
    total_cost = ferris_wheel_cost + roller_coaster_cost + bumper_cars_cost

    # Calculate how many more tickets Jeanne needs to buy
    more_tickets_needed = total_cost - current_tickets
    result = more_tickets_needed
    return result

print(solution())
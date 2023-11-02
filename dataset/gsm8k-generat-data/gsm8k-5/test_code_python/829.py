def solution():
    ferris_wheel_cost = 5  # The Ferris wheel costs 5 tickets
    roller_coaster_cost = 4  # The roller coaster costs 4 tickets
    bumper_cars_cost = 4  # The bumper cars cost 4 tickets
    available_tickets = 5  # Jeanne has 5 tickets

    # Calculate the total cost of all three rides
    total_cost = ferris_wheel_cost + roller_coaster_cost + bumper_cars_cost

    # Determine how many more tickets Jeanne needs to buy
    additional_tickets = total_cost - available_tickets
    result = additional_tickets
    return result

print(solution())
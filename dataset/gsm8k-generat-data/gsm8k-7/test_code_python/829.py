def solution():
    ferris_wheel_cost = 5
    roller_coaster_cost = 4
    bumper_cars_cost = 4
    num_tickets = 5

    # Calculate the total cost of all the rides that Jeanne wants to go on
    total_cost = ferris_wheel_cost + roller_coaster_cost + bumper_cars_cost

    # Calculate how many more tickets Jeanne needs to buy
    num_extra_tickets = total_cost - num_tickets
    result = num_extra_tickets
    return result

print(solution())
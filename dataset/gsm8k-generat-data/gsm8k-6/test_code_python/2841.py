def solution():
    ferris_wheel_rides = 2  # number of times Dolly wants to ride Ferris wheel
    roller_coaster_rides = 3  # number of times Dolly wants to ride roller coaster
    log_ride_rides = 7  # number of times Dolly wants to ride log ride
    ferris_wheel_cost = 2  # cost of one Ferris wheel ride in tickets
    roller_coaster_cost = 5  # cost of one roller coaster ride in tickets
    log_ride_cost = 1  # cost of one log ride in tickets
    available_tickets = 20  # number of tickets Dolly has

    # Calculate the total cost of all the rides
    total_cost = ferris_wheel_rides * ferris_wheel_cost + \
                 roller_coaster_rides * roller_coaster_cost + \
                 log_ride_rides * log_ride_cost

    # Calculate the additional tickets Dolly needs to buy
    additional_tickets = total_cost - available_tickets
    result = additional_tickets
    return result

print(solution())
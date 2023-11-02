def solution():
    rollercoaster_tickets = 4
    catapult_tickets = 4
    ferris_wheel_tickets = 1
    num_rollercoaster_rides = 3
    num_catapult_rides = 2
    num_ferris_wheel_rides = 1

    # Calculate the total number of tickets for all rollercoaster rides
    total_rollercoaster_tickets = rollercoaster_tickets * num_rollercoaster_rides

    # Calculate the total number of tickets for all Catapult rides
    total_catapult_tickets = catapult_tickets * num_catapult_rides

    # Calculate the total number of tickets for all Ferris wheel rides
    total_ferris_wheel_tickets = ferris_wheel_tickets * num_ferris_wheel_rides

    # Calculate the total number of tickets needed for all rides
    total_tickets = total_rollercoaster_tickets + total_catapult_tickets + total_ferris_wheel_tickets
    result = total_tickets
    return result

print(solution())
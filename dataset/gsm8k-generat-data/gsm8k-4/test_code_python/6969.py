def solution():
    """Turner wants to ride the rollercoaster 3 times, the Catapult 2 times and the Ferris wheel once. It costs 4 tickets to ride the rollercoaster, 4 tickets to ride the Catapult and 1 ticket to ride the Ferris wheel. How many tickets does Turner need?"""
    # Define the number of times Turner wants to ride each attraction
    rollercoaster_rides = 3
    catapult_rides = 2
    ferris_wheel_rides = 1

    # Define the cost of each attraction
    rollercoaster_cost = 4
    catapult_cost = 4
    ferris_wheel_cost = 1

    # Calculate the total number of tickets needed
    total_tickets = (rollercoaster_rides * rollercoaster_cost) + \
                    (catapult_rides * catapult_cost) + \
                    (ferris_wheel_rides * ferris_wheel_cost)

    result = total_tickets
    return result

print(solution())
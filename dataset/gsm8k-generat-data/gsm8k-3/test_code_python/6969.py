def solution():
    """Turner wants to ride the rollercoaster 3 times, the Catapult 2 times and the Ferris wheel once. It costs 4 tickets to ride the rollercoaster, 4 tickets to ride the Catapult and 1 ticket to ride the Ferris wheel. How many tickets does Turner need?"""
    # Define the cost of each ride in tickets
    ROLLERCOASTER_COST = 4
    CATAPULT_COST = 4
    FERRIS_WHEEL_COST = 1

    # Define the number of times Turner wants to ride each ride
    rollercoaster_rides = 3
    catapult_rides = 2
    ferris_wheel_rides = 1

    # Calculate the total number of tickets needed
    total_tickets = (rollercoaster_rides * ROLLERCOASTER_COST) + (catapult_rides * CATAPULT_COST) + (ferris_wheel_rides * FERRIS_WHEEL_COST)

    # Display the total number of tickets needed
    result = total_tickets
    return result

print(solution())
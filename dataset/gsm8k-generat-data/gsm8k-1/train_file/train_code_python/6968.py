def solution():
    """Turner wants to ride the rollercoaster 3 times, the Catapult 2 times and the Ferris wheel once. It costs 4 tickets to ride the rollercoaster, 4 tickets to ride the Catapult and 1 ticket to ride the Ferris wheel. How many tickets does Turner need?"""
    rollercoaster_tickets = 4
    catapult_tickets = 4
    ferris_wheel_tickets = 1
    rollercoaster_rides = 3
    catapult_rides = 2
    ferris_wheel_rides = 1
    total_tickets = rollercoaster_tickets * rollercoaster_rides + catapult_tickets * catapult_rides + ferris_wheel_tickets * ferris_wheel_rides
    result = total_tickets
    return result

print(solution())
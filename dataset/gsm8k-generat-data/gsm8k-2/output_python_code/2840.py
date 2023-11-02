def solution():
    """Dolly wants to ride the Ferris wheel twice, the roller coaster three times, and the log ride seven times. The Ferris wheel costs 2 tickets, the roller coaster costs 5 tickets and the log ride costs 1 ticket. Dolly has 20 tickets. How many more tickets should Dolly buy?"""
    ferris_wheel_tickets = 2
    roller_coaster_tickets = 5
    log_ride_tickets = 1
    ferris_wheel_rides = 2
    roller_coaster_rides = 3
    log_ride_rides = 7
    total_tickets_needed = ferris_wheel_tickets * ferris_wheel_rides + roller_coaster_tickets * roller_coaster_rides + log_ride_tickets * log_ride_rides
    tickets_to_buy = total_tickets_needed - 20
    result = tickets_to_buy
    return result

print(solution())
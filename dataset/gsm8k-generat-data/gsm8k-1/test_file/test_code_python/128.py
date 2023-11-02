def solution():
    """Pam and Fred went to a carnival. Pam rode the roller coaster 2 times while Fred rode it 4 times. After that, each of them decided to ride the luge 2 times. If each ride cost 6 tickets, how many tickets did they use that day?"""
    roller_coaster_rides = 2 + 4
    luge_rides = 2 * 2
    ticket_cost_per_ride = 6
    total_tickets_used = roller_coaster_rides * ticket_cost_per_ride + luge_rides * ticket_cost_per_ride
    result = total_tickets_used
    return result

print(solution())
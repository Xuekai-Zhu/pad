def solution():
    
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
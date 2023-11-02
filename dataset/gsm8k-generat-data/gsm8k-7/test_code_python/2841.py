def solution():
    ferris_wheel_cost = 2
    roller_coaster_cost = 5
    log_ride_cost = 1

    num_ferris_wheel_rides = 2
    num_roller_coaster_rides = 3
    num_log_rides = 7

    total_tickets_needed = (num_ferris_wheel_rides * ferris_wheel_cost) + (
                num_roller_coaster_rides * roller_coaster_cost) + (num_log_rides * log_ride_cost)

    tickets_to_buy = total_tickets_needed - 20
    result = tickets_to_buy
    return result

print(solution())
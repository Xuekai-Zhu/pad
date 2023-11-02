def solution():
    ferris_wheel_tickets = 2  # Dolly needs 2 tickets to ride the Ferris wheel once
    roller_coaster_tickets = 5  # Dolly needs 5 tickets to ride the roller coaster once
    log_ride_tickets = 1  # Dolly needs 1 ticket to ride the log ride once
    total_ferris_wheel_tickets = ferris_wheel_tickets * 2  # Dolly wants to ride the Ferris wheel twice
    total_roller_coaster_tickets = roller_coaster_tickets * 3  # Dolly wants to ride the roller coaster three times
    total_log_ride_tickets = log_ride_tickets * 7  # Dolly wants to ride the log ride seven times

    # Calculate the total number of tickets Dolly needs
    total_tickets = total_ferris_wheel_tickets + total_roller_coaster_tickets + total_log_ride_tickets

    # Calculate the number of tickets Dolly needs to buy
    tickets_to_buy = total_tickets - 20
    result = tickets_to_buy
    return result

print(solution())
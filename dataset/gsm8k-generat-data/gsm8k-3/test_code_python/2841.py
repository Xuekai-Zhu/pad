def solution():
    """Dolly wants to ride the Ferris wheel twice, the roller coaster three times, and the log ride seven times. The Ferris wheel costs 2 tickets, the roller coaster costs 5 tickets and the log ride costs 1 ticket. Dolly has 20 tickets. How many more tickets should Dolly buy?"""
    # Define the number of times Dolly wants to ride each ride
    ferris_wheel_rides = 2
    roller_coaster_rides = 3
    log_ride_rides = 7

    # Define the cost of each ride
    ferris_wheel_cost = 2
    roller_coaster_cost = 5
    log_ride_cost = 1

    # Define the number of tickets Dolly has
    tickets = 20

    # Calculate the total cost of all the rides
    total_cost = (ferris_wheel_rides * ferris_wheel_cost) + \
                 (roller_coaster_rides * roller_coaster_cost) + \
                 (log_ride_rides * log_ride_cost)

    # Calculate the number of tickets Dolly needs to buy
    tickets_needed = total_cost - tickets

    # Display the number of tickets Dolly needs to buy
    result = tickets_needed
    return result

print(solution())
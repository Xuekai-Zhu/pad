def solution():
    # Define the number of times Dolly wants to ride each ride
    ferris_wheel_rides = 2
    roller_coaster_rides = 3
    log_ride_rides = 7

    # Define the cost of each ride
    ferris_wheel_cost = 2
    roller_coaster_cost = 5
    log_ride_cost = 1

    # Define Dolly's total budget of tickets
    total_budget = 20

    # Calculate the total cost of all of Dolly's planned rides
    total_cost = (ferris_wheel_rides * ferris_wheel_cost) + (roller_coaster_rides * roller_coaster_cost) + (log_ride_rides * log_ride_cost)

    # Calculate how many more tickets Dolly needs to buy
    more_tickets = total_cost - total_budget
    result = more_tickets
    return result

print(solution())
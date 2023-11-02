def solution():
    """Paula wants to ride the go-karts 1 time and the bumper cars 4 times. It costs 4 tickets to ride the go-karts and 5 tickets to ride the bumper cars. How many tickets does Paula need?"""
    # Define the number of rides Paula wants to take
    go_kart_rides = 1
    bumper_car_rides = 4

    # Define the ticket cost for each ride
    go_kart_ticket_cost = 4
    bumper_car_ticket_cost = 5

    # Calculate the total number of tickets needed
    total_tickets = (go_kart_rides * go_kart_ticket_cost) + (bumper_car_rides * bumper_car_ticket_cost)

    # return the result
    result = total_tickets
    return result

print(solution())
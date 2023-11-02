def solution():
    """Paula wants to ride the go-karts 1 time and the bumper cars 4 times.
    It costs 4 tickets to ride the go-karts and 5 tickets to ride the bumper cars.
    How many tickets does Paula need?"""
    # Define the cost of each ride
    GO_KART_PRICE = 4
    BUMPER_CAR_PRICE = 5

    # Define the number of rides Paula wants to take
    go_kart_rides = 1
    bumper_car_rides = 4

    # Calculate the total number of tickets Paula needs
    total_tickets = go_kart_rides * GO_KART_PRICE + bumper_car_rides * BUMPER_CAR_PRICE

    # Display the total number of tickets
    result = total_tickets
    return result

print(solution())
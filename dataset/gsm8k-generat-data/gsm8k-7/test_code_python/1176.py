def solution():
    go_kart_tickets = 4  # Cost of one go-kart ride
    bumper_car_tickets = 5  # Cost of one bumper car ride
    num_go_kart_rides = 1
    num_bumper_car_rides = 4

    # Calculate the total number of tickets needed
    total_tickets = (go_kart_tickets * num_go_kart_rides) + (bumper_car_tickets * num_bumper_car_rides)
    result = total_tickets
    return result

print(solution())
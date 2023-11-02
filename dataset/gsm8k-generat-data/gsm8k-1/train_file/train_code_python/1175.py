def solution():
    """Paula wants to ride the go-karts 1 time and the bumper cars 4 times. It costs 4 tickets to ride the go-karts and 5 tickets to ride the bumper cars. How many tickets does Paula need?"""
    go_kart_cost = 4
    bumper_car_cost = 5
    go_kart_rides = 1
    bumper_car_rides = 4
    total_tickets = (go_kart_cost * go_kart_rides) + (bumper_car_cost * bumper_car_rides)
    result = total_tickets
    return result

print(solution())
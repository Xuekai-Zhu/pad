def solution():
    total_money = 17.80
    num_toy_cars = 4
    toy_car_price = 0.95
    race_track_price = 6.00

    # Calculate the total cost of all toy cars
    total_toy_cars_cost = num_toy_cars * toy_car_price

    # Calculate the total cost of all purchased items
    total_cost = total_toy_cars_cost + race_track_price

    # Calculate the remaining money after the purchases
    remaining_money = total_money - total_cost
    result = remaining_money
    return result

print(solution())
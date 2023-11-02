def solution():
    num_toy_cars = 2
    toy_car_price = 11
    scarf_price = 10
    beanie_price = 14
    remaining_money = 7

    # Calculate the cost of the 2 toy cars
    toy_cars_cost = num_toy_cars * toy_car_price

    # Calculate the total cost of all items except the remaining money
    total_cost = toy_cars_cost + scarf_price + beanie_price

    # Calculate the starting amount of money
    starting_amount = total_cost + remaining_money
    result = starting_amount
    return result

print(solution())
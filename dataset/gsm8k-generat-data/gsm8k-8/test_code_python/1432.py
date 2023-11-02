def solution():
    # Calculate the cost of the car as a percentage of the original price
    car_cost_percentage = 40

    # Calculate the cost of the car as a decimal of the original price
    car_cost_decimal = car_cost_percentage / 100

    # Calculate the original price of the car
    original_price = 15000 / car_cost_decimal
    result = original_price
    return result

print(solution())
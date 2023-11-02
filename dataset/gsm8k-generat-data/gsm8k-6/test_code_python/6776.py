def solution():
    # Calculate the amount Liz received from selling her car
    original_price = 100  # assume Liz originally paid $100 for her car
    sale_price = 80  # Liz sold her car at 80% of the original price
    proceeds = (sale_price/100) * original_price

    # Calculate the amount Liz needs to pay for her new car
    new_car_price = 30000
    difference = new_car_price - proceeds - 4000  # Liz uses the proceeds from the car sale and needs an additional $4000

    result = difference
    return result

print(solution())
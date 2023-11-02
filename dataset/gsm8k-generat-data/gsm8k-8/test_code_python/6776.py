def solution():
    # Calculate the amount Liz sold her old car for
    old_car_sale_price = 0.8 * original_car_price

    # Calculate the total amount Liz has for her new car
    total_amount_for_new_car = old_car_sale_price + 4000

    # Calculate the difference between what Liz paid for her old car and the cost of the new car
    cost_difference = original_car_price - 30000

    # Calculate how much cheaper the new car is compared to the old one
    cheaper_amount = cost_difference - total_amount_for_new_car

    result = cheaper_amount
    return result

print(solution())
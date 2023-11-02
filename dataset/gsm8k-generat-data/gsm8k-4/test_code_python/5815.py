def solution():
    """Eunice spent $7500 on a used car, which is 25% less than the original price. What was the original price of the car?"""
    # Define the price of the used car and the percentage decrease
    used_car_price = 7500
    percentage_decrease = 25

    # Calculate the original price of the car
    original_price = used_car_price / (1 - percentage_decrease/100)

    result = original_price
    return result

print(solution())
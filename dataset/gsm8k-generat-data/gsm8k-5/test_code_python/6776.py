def solution():
    # Calculate how much Liz sold her car for
    original_price = 100  # Assume that Liz originally paid $100 for her car
    sold_price = original_price * 0.8  # Liz sold her car for 80% of the original price

    # Calculate how much Liz needs to pay for her new car
    new_car_price = 30000  # Liz wants to buy a car that costs $30,000
    amount_needed = new_car_price - sold_price  # Liz will use the proceeds from selling her old car and needs this much more to buy the new car

    # Calculate how much cheaper the new car is compared to what Liz originally paid
    difference = original_price - amount_needed

    result = difference
    return result

print(solution())
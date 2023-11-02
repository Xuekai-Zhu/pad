def solution():
    # Calculate the price of the SUV
    suv_price = 2 * 30000  # the SUV is twice as expensive as the coupe
    total_price = suv_price + 30000  # total price of both cars
    commission = 0.02 * total_price  # Melissa's commission is 2% of the total price
    result = commission
    return result

print(solution())
def solution():
    """Melissa sells a coupe for $30,000 and an SUV for twice as much. If her commission is 2%, how much money did she make from these sales?"""
    # Define the price of the coupe and the SUV
    coupe_price = 30000
    suv_price = 2 * coupe_price

    # Calculate Melissa's commission for each sale
    coupe_commission = 0.02 * coupe_price
    suv_commission = 0.02 * suv_price

    # Calculate Melissa's total commission
    total_commission = coupe_commission + suv_commission

    # Display Melissa's total commission
    result = total_commission
    return result

print(solution())
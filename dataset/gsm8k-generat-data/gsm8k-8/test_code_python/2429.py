def solution():
    # Define the price and quantity for each seller
    bea_price = 25
    dawn_price = 28
    bea_quantity = 10
    dawn_quantity = 8

    # Calculate the total earnings for each seller
    bea_earnings = bea_price * bea_quantity
    dawn_earnings = dawn_price * dawn_quantity

    # Calculate the difference in earnings
    earnings_difference = bea_earnings - dawn_earnings
    result = earnings_difference
    return result

print(solution())
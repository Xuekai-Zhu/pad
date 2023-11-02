def solution():
    # Define the prices of the different items
    price_per_cupcake = 1.5
    price_per_cookie_packet = 2
    price_per_biscuit_packet = 1

    # Calculate the total earnings per day
    earnings_per_day = (20 * price_per_cupcake) + (10 * price_per_cookie_packet) + (20 * price_per_biscuit_packet)

    # Calculate the total earnings for five days
    total_earnings = 5 * earnings_per_day
    result = total_earnings
    return result

print(solution())
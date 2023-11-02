def solution():
    # Calculate the discounted prices for both flights
    delta_discounted_price = 0.8 * 850
    united_discounted_price = 0.7 * 1100

    # Determine which flight is cheaper
    if delta_discounted_price < united_discounted_price:
        savings = united_discounted_price - delta_discounted_price
    else:
        savings = 0

    result = savings
    return result

print(solution())
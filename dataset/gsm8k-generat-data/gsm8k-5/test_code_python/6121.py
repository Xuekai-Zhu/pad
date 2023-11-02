def solution():
    # Calculate the discounted prices for Delta and United flights
    delta_discounted = 850 * 0.8  # Delta Airlines offers a 20% discount on the $850 flight
    united_discounted = 1100 * 0.7  # United Airlines offers a 30% discount on the $1100 flight

    # Determine which flight is cheaper
    if delta_discounted < united_discounted:
        cheapest_price = delta_discounted
    else:
        cheapest_price = united_discounted

    # Calculate how much money Carrie would save by choosing the cheapest flight
    delta_savings = 850 - delta_discounted
    united_savings = 1100 - united_discounted

    if cheapest_price == delta_discounted:
        savings = delta_savings
    else:
        savings = united_savings

    result = savings
    return result

print(solution())
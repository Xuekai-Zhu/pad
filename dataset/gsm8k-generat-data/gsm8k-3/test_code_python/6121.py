def solution():
    """Carrie wants to take a trip to New York. She can get a 20% discount on an $850 flight with Delta Airlines. She can also save 30% off an $1100 flight with United Airlines. How much money would she save by choosing the cheapest flight?"""
    # Calculate the discounted prices for each airline
    delta_discount = 0.2 * 850
    delta_price = 850 - delta_discount

    united_discount = 0.3 * 1100
    united_price = 1100 - united_discount

    # Determine which flight is cheaper
    if delta_price < united_price:
        saved_money = united_discount
    else:
        saved_money = delta_discount

    # Display the amount of money saved
    result = saved_money
    return result

print(solution())
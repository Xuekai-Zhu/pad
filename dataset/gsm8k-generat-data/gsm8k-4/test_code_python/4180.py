def solution():
    """Maria buys a large bar of French soap that lasts her for 2 months. She spends $8.00 per bar of soap. If she wants to stock up for the entire year, how much will she spend on soap?"""
    # Define the price and lifespan of a bar of soap
    soap_price = 8
    soap_lifespan = 2  # in months

    # Calculate the number of bars of soap needed for a year
    bars_per_year = 12 / soap_lifespan

    # Calculate the total cost of the soap for a year
    total_cost = bars_per_year * soap_price

    # return the result
    result = total_cost
    return result

print(solution())
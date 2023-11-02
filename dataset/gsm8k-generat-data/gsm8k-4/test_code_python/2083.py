def solution():
    """James buys pistachios for $10 per can. Each can is 5 ounces. He eats 30 ounces of pistachios every 5 days. How much does he spend on pistachios per week?"""
    # Define the price and weight of a can of pistachios
    PISTACHIO_PRICE = 10
    PISTACHIO_WEIGHT = 5

    # Calculate the number of cans James eats in 5 days
    cans_per_5_days = 30 / PISTACHIO_WEIGHT

    # Calculate the cost of the pistachios James eats in 5 days
    cost_per_5_days = cans_per_5_days * PISTACHIO_PRICE

    # Calculate the cost of pistachios per week
    cost_per_week = cost_per_5_days * 7 / 5

    # return the result
    result = cost_per_week
    return result

print(solution())
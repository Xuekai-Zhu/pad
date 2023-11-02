def solution():
    """Barbara asked the butcher for 4 1/2 pound steaks that cost $15.00/pound. She also asked for a pound and half of chicken breasts that were $8.00 a pound. How much did she spend at the butchers?"""
    # Define the price of steaks and the number of pounds requested
    steak_price = 15.00
    steak_pounds = 4.5

    # Define the price of chicken breasts and the number of pounds requested
    chicken_price = 8.00
    chicken_pounds = 1.5

    # Calculate the total cost of steaks
    steak_cost = steak_price * steak_pounds

    # Calculate the total cost of chicken breasts
    chicken_cost = chicken_price * chicken_pounds

    # Calculate the total cost of the purchase
    total_cost = steak_cost + chicken_cost

    # return the result
    result = total_cost
    return result

print(solution())
def solution():
    """Wally buys bears at the park. A bear is priced at $4.00 for the first bear and a discount of 50 cents per bear is given after that. How much does Wally pay for 101 bears?"""
    # Define the price for the first bear and the discount rate for additional bears
    first_bear_price = 4
    discount_rate = 0.5

    # Calculate the total price for 101 bears
    total_price = first_bear_price + (discount_rate * 100)

    # return the result
    result = total_price
    return result

print(solution())
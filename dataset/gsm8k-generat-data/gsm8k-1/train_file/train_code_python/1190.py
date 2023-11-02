def solution():
    """Wally buys bears at the park. A bear is priced at $4.00 for the first bear and a discount of 50 cents per bear is given after that. How much does Wally pay for 101 bears?"""
    first_bear_price = 4.00
    discount = 0.50
    additional_bears = 100
    additional_bear_price = first_bear_price - discount
    total_price = (first_bear_price + additional_bear_price * additional_bears)
    result = total_price
    return result

print(solution())
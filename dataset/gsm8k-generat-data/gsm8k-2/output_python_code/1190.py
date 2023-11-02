def solution():
    """Wally buys bears at the park. A bear is priced at $4.00 for the first bear and a discount of 50 cents per bear is given after that. How much does Wally pay for 101 bears?"""
    first_bear_price = 4.00
    discount_per_bear = 0.50
    total_bears = 101
    total_price = 0
    for i in range(total_bears):
        if i == 0:
            total_price += first_bear_price
        else:
            total_price += first_bear_price - (discount_per_bear * i)

    result = total_price
    return result

print(solution())
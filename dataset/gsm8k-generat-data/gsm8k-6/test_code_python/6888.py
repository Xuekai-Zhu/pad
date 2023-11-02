def solution():
    # Find the cost of one pint of strawberries on sale
    sale_price = 216 / 54  # they made $216 selling 54 pints
    # Find the cost of one pint of strawberries not on sale
    regular_price = sale_price + 108/54  # $108 less than they would have made selling the same number of pints without the sale
    # Find the difference in cost between a pint of strawberries on sale and not on sale
    price_difference = regular_price - sale_price
    result = price_difference
    return result

print(solution())
def solution():
    """A supermarket has pints of strawberries on sale. They sold 54 pints and made $216, which was $108 less than they would have made selling the same number of pints without the sale. How many more dollars does a pint of strawberries cost when not on sale?"""
    sale_price = 4  # assume sale price is $4 per pint
    num_pints = 54
    sale_revenue = 216
    regular_price = (sale_revenue + 108) / num_pints  # revenue per pint without sale
    difference = regular_price - sale_price
    result = difference
    return result

print(solution())
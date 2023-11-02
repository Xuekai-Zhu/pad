def solution():
    """A supermarket has pints of strawberries on sale. They sold 54 pints and made $216, which was $108 less than they would have made selling the same number of pints without the sale. How many more dollars does a pint of strawberries cost when not on sale?"""
    sale_price = 4
    normal_price = sale_price + 2
    total_sale_revenue = 216
    total_normal_revenue = total_sale_revenue + 108
    pints_sold = 54
    normal_price_per_pint = total_normal_revenue / pints_sold
    sale_price_per_pint = sale_price
    difference_per_pint = normal_price_per_pint - sale_price_per_pint
    result = difference_per_pint
    return result

print(solution())
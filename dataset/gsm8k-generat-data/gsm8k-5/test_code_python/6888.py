def solution():
    # Let x be the cost of one pint of strawberries without the sale
    # Then the revenue from selling 54 pints without the sale would be 54x
    # The revenue from selling 54 pints with the sale is $216, or (54-x)*4
    # We also know that (54-x)*4 = (54x-108), because the sale price is $4 less than the original price
    # Solving for x gives x = 6, which is the cost of one pint of strawberries without the sale
    # So the difference in cost between a pint on sale and not on sale is $4
    result = 4
    return result

print(solution())
def solution():
    # Define the variables
    sold_pints = 54
    sale_revenue = 216
    regular_revenue = sale_revenue + 108

    # Calculate the price difference per pint
    price_diff = (regular_revenue - sale_revenue) / sold_pints

    result = price_diff
    return result

print(solution())
def solution():
    num_pints = 54
    sale_revenue = 216
    regular_revenue = sale_revenue + 108

    # Calculate the price per pint for sale and regular price
    sale_price_per_pint = sale_revenue / num_pints
    regular_price_per_pint = regular_revenue / num_pints

    # Calculate the price difference per pint when not on sale
    price_difference = regular_price_per_pint - sale_price_per_pint
    result = price_difference
    return result

print(solution())
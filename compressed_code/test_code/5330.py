def solution():
    
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
def solution():
    
    jay_guests = 22
    gloria_guests = 36
    total_guests = jay_guests + gloria_guests
    total_flags = total_guests + 2
    flags_per_sale = 5
    sale_price = 1.00
    total_sales = total_flags / flags_per_sale
    total_cost = total_sales * sale_price
    result = total_cost
    return result

print(solution())
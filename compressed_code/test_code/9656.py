def solution():
    
    sale_price = 500000 * 1.2
    revenue_per_person = sale_price / 4
    revenue_after_tax = revenue_per_person * 0.9
    result = round(revenue_after_tax, 2)
    return result

print(solution())
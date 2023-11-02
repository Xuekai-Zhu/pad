def solution():
    """James sells a $500,000 house for 20% over market value. He splits the revenue with his 3 brothers. How much does each person get after taxes take away 10%?"""
    sale_price = 500000 * 1.2
    revenue_per_person = sale_price / 4
    revenue_after_tax = revenue_per_person * 0.9
    result = round(revenue_after_tax, 2)
    return result

print(solution())
def solution():
    """James sells a $500,000 house for 20% over market value. He splits the revenue with his 3 brothers. How much does each person get after taxes take away 10%?"""
    house_price = 500000
    market_value = house_price / 1.2
    selling_price = 1.2 * market_value
    revenue_per_person = (selling_price / 4) * 0.9
    result = revenue_per_person
    return result

print(solution())
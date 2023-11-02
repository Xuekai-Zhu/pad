def solution():
    """Nigella is a realtor who earns a base salary of $3,000 a month plus a 2% commission on every house she sells. One month, Nigella sells 3 houses and earns $8,000 total. House B costs three times as much as House A. House C cost twice as much as House A minus $110,000. How much did House A cost?"""
    base_salary = 3000
    total_earnings = 8000
    commission_rate = 0.02
    num_houses_sold = 3
    commission_earned = total_earnings - base_salary
    avg_sale_price = commission_earned / (num_houses_sold * commission_rate)
    price_b = avg_sale_price * 3
    price_c = (2 * avg_sale_price) - 110000
    price_a = (total_earnings - (price_b + price_c)) / 3
    result = price_a
    return result

print(solution())
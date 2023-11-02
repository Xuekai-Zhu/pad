def solution():
    """Nigella is a realtor who earns a base salary of $3,000 a month plus a 2% commission on every house she sells. One month, Nigella sells 3 houses and earns $8,000 total. House B costs three times as much as House A. House C cost twice as much as House A minus $110,000. How much did House A cost?"""
    base_salary = 3000
    commission_rate = 0.02
    total_earnings = 8000
    num_houses_sold = 3
    commission_earnings = (total_earnings - base_salary) / commission_rate
    commission_per_house = commission_earnings / num_houses_sold
    house_c_cost = (commission_per_house * 0.5) + 110000
    house_b_cost = house_c_cost * 3
    house_a_cost = (commission_per_house - house_c_cost - house_b_cost) / (-3)
    result = house_a_cost
    return result

print(solution())
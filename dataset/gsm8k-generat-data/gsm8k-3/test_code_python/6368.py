def solution():
    """Nigella is a realtor who earns a base salary of $3,000 a month plus a 2% commission on every house she sells. One month, Nigella sells 3 houses and earns $8,000 total. House B costs three times as much as House A. House C cost twice as much as House A minus $110,000. How much did House A cost?"""
    # Define Nigella's base salary and commission rate
    BASE_SALARY = 3000
    COMMISSION_RATE = 0.02

    # Define the cost of each house
    cost_a = x
    cost_b = 3 * cost_a
    cost_c = 2 * (cost_a - 110000)

    # Solve for x (the cost of House A)
    total_commission = 8000 - BASE_SALARY
    commission_per_sale = total_commission / 3
    commission_rate = commission_per_sale / cost_a
    x = commission_rate / COMMISSION_RATE

    # Return the cost of House A
    result = cost_a
    return result

print(solution())
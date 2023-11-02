def solution():
    """Janet wanted to move out of her parents' house and rent her own apartment. She had $2,225 saved. She found an apartment that cost $1,250 per month that was perfect for her. The landlord said that she needed to be able to pay 2 months' rent in advance to rent the place and she would also need to put down a deposit of $500. How much more money did Janet need in order to rent the apartment?"""
    savings = 2225
    rent_per_month = 1250
    months_advance = 2
    deposit = 500
    total_cost = (rent_per_month * months_advance) + deposit
    amount_needed = total_cost - savings
    result = amount_needed
    return result

print(solution())
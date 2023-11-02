def solution():
    """Janet wanted to move out of her parents' house and rent her own apartment. She had $2,225 saved. She found an apartment that cost $1,250 per month that was perfect for her. The landlord said that she needed to be able to pay 2 months' rent in advance to rent the place and she would also need to put down a deposit of $500. How much more money did Janet need in order to rent the apartment?"""
    total_deposit = 500
    advance_rent = 2 * 1250
    total_cost = total_deposit + advance_rent
    janet_saved = 2225
    remaining_cost = total_cost - janet_saved
    result = remaining_cost
    return result

print(solution())
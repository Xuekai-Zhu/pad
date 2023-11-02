def solution():
    """If Lyn donates $240 to a private organization each year where 1/3 of it goes to the community pantry project,
    1/2 goes to the local crisis fund, 1/4 of the remaining goes to livelihood project funds, and the rest is for contingency funds.
    How much goes to contingency fund?"""
    donation_amount = 240
    pantry_fund = donation_amount / 3
    crisis_fund = donation_amount / 2
    remaining_fund = donation_amount - (pantry_fund + crisis_fund)
    livelihood_fund = remaining_fund / 4
    contingency_fund = remaining_fund - livelihood_fund
    result = contingency_fund
    return result

print(solution())
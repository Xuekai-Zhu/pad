def solution():
    """If Lyn donates $240 to a private organization each year where 1/3 of it goes to the community pantry project,
    1/2 goes to the local crisis fund, 1/4 of the remaining goes to livelihood project funds, and the rest is for contingency funds.
    How much goes to contingency fund?"""
    total_donation = 240
    pantry_fund = total_donation * (1/3)
    crisis_fund = total_donation * (1/2)
    remaining_fund = total_donation - (pantry_fund + crisis_fund)
    livelihood_fund = remaining_fund * (1/4)
    contingency_fund = remaining_fund - livelihood_fund
    result = contingency_fund
    return result

print(solution())
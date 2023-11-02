def solution():
    
    donation_amount = 240
    pantry_fund = donation_amount / 3
    crisis_fund = donation_amount / 2
    remaining_fund = donation_amount - (pantry_fund + crisis_fund)
    livelihood_fund = remaining_fund / 4
    contingency_fund = remaining_fund - livelihood_fund
    result = contingency_fund
    return result

print(solution())
def solution():
    donation = 240  # Lyn donates $240 each year
    pantry_fund = donation * (1/3)  # 1/3 of the donation goes to the community pantry project
    crisis_fund = donation * (1/2)  # 1/2 of the donation goes to the local crisis fund
    remaining_fund = donation - pantry_fund - crisis_fund  # Calculate the remaining fund
    livelihood_fund = remaining_fund * (1/4)  # 1/4 of the remaining fund goes to livelihood project funds
    contingency_fund = remaining_fund - livelihood_fund  # The rest goes to contingency funds
    result = contingency_fund
    return result

print(solution())
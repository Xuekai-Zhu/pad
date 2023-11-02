def solution():
    """Holly gets 26 paychecks per year. If she puts $100.00 from every paycheck into her 401K, her company will match that contribution by 6%. How much money has she and her company contributed to her 401k after 1 year?"""
    num_of_paychecks = 26
    personal_contribution = 100.00
    company_match_percentage = 0.06
    total_contribution = (personal_contribution + (personal_contribution * company_match_percentage)) * num_of_paychecks
    result = total_contribution
    return result

print(solution())
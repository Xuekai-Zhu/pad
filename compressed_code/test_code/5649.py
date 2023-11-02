def solution():
    
    num_of_paychecks = 26
    personal_contribution = 100.00
    company_match_percentage = 0.06
    total_contribution = (personal_contribution + (personal_contribution * company_match_percentage)) * num_of_paychecks
    result = total_contribution
    return result

print(solution())
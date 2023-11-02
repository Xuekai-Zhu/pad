def solution():
    total_paychecks = 26
    paycheck_contribution = 100
    company_match_percent = 6
    
    total_contribution = total_paychecks * (paycheck_contribution + (paycheck_contribution * (company_match_percent / 100)))
    
    return total_contribution

print(solution())
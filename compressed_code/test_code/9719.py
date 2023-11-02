def solution():
    
    months_until_vacation = 15
    total_savings_needed = 3000
    biweekly_paychecks = 2
    paychecks_until_vacation = months_until_vacation * biweekly_paychecks
    amount_per_paycheck = total_savings_needed / paychecks_until_vacation
    result = amount_per_paycheck
    return result

print(solution())
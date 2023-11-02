def solution():
    
    saving_goal = 3000
    saving_months = 15
    paychecks_per_month = 2
    total_paychecks = saving_months * paychecks_per_month
    amount_per_paycheck = saving_goal / total_paychecks
    result = amount_per_paycheck
    return result

print(solution())
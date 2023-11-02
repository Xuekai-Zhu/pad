def solution():
    total_savings_goal = 3000.0
    num_months_to_save = 15.0
    num_paychecks_per_month = 2.0

    # Calculate the total number of paychecks Jackson will receive
    total_paychecks = num_months_to_save * num_paychecks_per_month

    # Calculate the amount Jackson needs to save per paycheck
    amount_per_paycheck = total_savings_goal / total_paychecks
    result = amount_per_paycheck
    return result

print(solution())
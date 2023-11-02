def solution():
    time_in_months = 15  # Jackson wants to save for 15 months
    target_savings = 3000  # Jackson wants to save $3000 in total
    paychecks_per_month = 2  # Jackson gets paid twice a month

    # Calculate the total number of paychecks Jackson will receive during the savings period
    total_paychecks = time_in_months * paychecks_per_month

    # Calculate the amount Jackson needs to save per paycheck to reach his goal
    savings_per_paycheck = target_savings / total_paychecks
    result = savings_per_paycheck
    return result

print(solution())
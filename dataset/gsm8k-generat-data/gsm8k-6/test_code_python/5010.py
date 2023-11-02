def solution():
    # Calculate the amount Jackson needs to set aside per paycheck to save $3,000 in 15 months
    total_paychecks = 2 * 15  # Jackson gets paid 2 times a month for 15 months
    money_per_paycheck = 3000 / total_paychecks  # Jackson needs to save $3,000 in total
    result = money_per_paycheck
    return result

print(solution())
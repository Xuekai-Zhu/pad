def solution():
    # Define the number of months until the vacation and the total amount to save
    months_until_vacation = 15
    total_savings_goal = 3000

    # Calculate the number of paychecks Jackson will receive before the vacation
    paychecks_per_month = 2
    total_paychecks = months_until_vacation * paychecks_per_month

    # Calculate the amount that Jackson needs to save per paycheck
    amount_per_paycheck = total_savings_goal / total_paychecks
    result = amount_per_paycheck
    return result

print(solution())
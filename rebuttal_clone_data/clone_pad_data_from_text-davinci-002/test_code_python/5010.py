def solution():
    months_until_vacation = 15
    paychecks_per_month = 2
    money_needed = 3000
    money_per_paycheck = money_needed / (months_until_vacation * paychecks_per_month)
    result = money_per_paycheck
    return result

print(solution())
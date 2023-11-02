def solution():
    """Jackson wants to start saving for the vacation that he’s taking next August, 15 months away. He wants to save $3,000.00. If he gets paid 2 times a month how much money does he need to set aside, per paycheck, to have enough money saved for his vacation?"""
    months_until_vacation = 15
    total_savings_needed = 3000
    biweekly_paychecks = 2
    paychecks_until_vacation = months_until_vacation * biweekly_paychecks
    amount_per_paycheck = total_savings_needed / paychecks_until_vacation
    result = amount_per_paycheck
    return result

print(solution())
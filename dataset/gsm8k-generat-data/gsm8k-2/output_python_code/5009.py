def solution():
    """Jackson wants to start saving for the vacation that he’s taking next August, 15 months away. He wants to save $3,000.00. If he gets paid 2 times a month how much money does he need to set aside, per paycheck, to have enough money saved for his vacation?"""
    saving_goal = 3000
    saving_months = 15
    paychecks_per_month = 2
    total_paychecks = saving_months * paychecks_per_month
    amount_per_paycheck = saving_goal / total_paychecks
    result = amount_per_paycheck
    return result

print(solution())
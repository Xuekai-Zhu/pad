def solution():
    """Jackson wants to start saving for the vacation that he’s taking next August, 15 months away. He wants to save $3,000.00. If he gets paid 2 times a month how much money does he need to set aside, per paycheck, to have enough money saved for his vacation?"""
    # Define the total amount to save and the number of paychecks
    total_amount = 3000
    num_paychecks = 30

    # Calculate the amount to save per paycheck
    amount_per_paycheck = total_amount / num_paychecks

    # Round the amount to the nearest cent
    amount_per_paycheck = round(amount_per_paycheck, 2)

    result = amount_per_paycheck
    return result

print(solution())
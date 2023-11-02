def solution():
    """Jackson wants to start saving for the vacation that he’s taking next August, 15 months away.  He wants to save $3,000.00.  If he gets paid 2 times a month how much money does he need to set aside, per paycheck, to have enough money saved for his vacation?"""
    # Calculate the total number of paychecks Jackson will receive in the next 15 months
    num_paychecks = 2 * 15

    # Calculate the amount he needs to save per paycheck
    savings_per_paycheck = 3000 / num_paychecks

    # Display the amount he needs to save per paycheck
    result = savings_per_paycheck
    return result

print(solution())
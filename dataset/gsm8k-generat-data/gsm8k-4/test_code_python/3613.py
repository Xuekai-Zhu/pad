def solution():
    """The balance of Pam's bank account tripled during the year. At the end of the year, Pam withdrew $250. If her current balance is $950, how much did she have in the bank account at the beginning of the year?"""
    # Define the current balance and the amount withdrawn
    current_balance = 950
    withdrawn_amount = 250

    # Calculate the balance before withdrawal
    balance_before_withdrawal = current_balance + withdrawn_amount

    # Calculate the balance at the beginning of the year
    beginning_balance = balance_before_withdrawal / 3

    result = beginning_balance
    return result

print(solution())
def solution():
    """The balance of Pam's bank account tripled during the year. At the end of the year, Pam withdrew $250. If her current balance is $950, how much did she have in the bank account at the beginning of the year?"""
    # Define the amount Pam withdrew
    WITHDRAWAL = 250

    # Define Pam's current balance
    current_balance = 950

    # Calculate Pam's balance before the withdrawal
    balance_before_withdrawal = current_balance + WITHDRAWAL

    # Calculate Pam's balance at the start of the year
    balance_at_start_of_year = balance_before_withdrawal / 3

    # Display Pam's balance at the start of the year
    result = balance_at_start_of_year
    return result

print(solution())
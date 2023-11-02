def solution():
    current_balance = 950  # Pam's current balance is $950
    withdrawn_amount = 250  # Pam withdrew $250 at the end of the year

    # Calculate the balance before the withdrawal
    balance_before_withdrawal = current_balance + withdrawn_amount

    # Calculate the balance at the beginning of the year
    beginning_balance = balance_before_withdrawal / 3
    result = beginning_balance
    return result

print(solution())
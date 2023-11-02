def solution():
    current_balance = 950
    withdrawal = 250
    balance_before_withdrawal = current_balance + withdrawal

    # Calculate the balance before it tripled
    balance_before_triple = balance_before_withdrawal / 3

    # Calculate the balance at the beginning of the year
    beginning_balance = balance_before_triple - withdrawal
    result = beginning_balance
    return result

print(solution())
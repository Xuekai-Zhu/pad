def solution():
    """The balance of Pam's bank account tripled during the year. At the end of the year, Pam withdrew $250. If her current balance is $950, how much did she have in the bank account at the beginning of the year?"""
    current_balance = 950
    withdrawal_amount = 250
    starting_balance = current_balance + withdrawal_amount
    initial_balance = starting_balance / 3
    result = initial_balance
    return result

print(solution())
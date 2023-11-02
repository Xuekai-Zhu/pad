def solution():
    """The balance of Pam's bank account tripled during the year. At the end of the year, Pam withdrew $250. If her current balance is $950, how much did she have in the bank account at the beginning of the year?"""
    current_balance = 950
    withdrawn_amount = 250
    starting_balance = (current_balance + withdrawn_amount) / 3
    result = starting_balance
    return result

print(solution())
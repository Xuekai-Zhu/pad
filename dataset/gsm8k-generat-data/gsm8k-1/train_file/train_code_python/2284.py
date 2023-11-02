def solution():
    """Kendy made 2 online bank transactions. She transferred $60 to her mom and half that amount to her sister. As a result, her account now has $100 left in it. How much money was in the account before the transfer?"""
    amount_transferred_to_mom = 60
    amount_transferred_to_sister = amount_transferred_to_mom / 2
    remaining_balance = 100
    initial_balance = remaining_balance + amount_transferred_to_mom + amount_transferred_to_sister
    result = initial_balance
    return result

print(solution())
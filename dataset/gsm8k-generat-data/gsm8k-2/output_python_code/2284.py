def solution():
    """Kendy made 2 online bank transactions. She transferred $60 to her mom and half that amount to her sister. As a result, her account now has $100 left in it. How much money was in the account before the transfer?"""
    mom_transfer = 60
    sister_transfer = mom_transfer / 2
    remaining_balance = 100
    starting_balance = mom_transfer + sister_transfer + remaining_balance
    result = starting_balance
    return result

print(solution())
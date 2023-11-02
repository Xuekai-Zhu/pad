def solution():
    """Kendy made 2 online bank transactions. She transferred $60 to her mom and half that amount to her sister. As a result, her account now has $100 left in it. How much money was in the account before the transfer?"""
    # Calculate the total amount transferred
    total_transfer = 60 + (1/2)*60

    # Calculate the amount remaining in the account after the transfer
    remaining = 100

    # Calculate the amount before the transfer
    before_transfer = total_transfer + remaining

    result = before_transfer
    return result

print(solution())
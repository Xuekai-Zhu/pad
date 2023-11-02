def solution():
    """If Jenna has twice as much money in her bank account as Phil does, and Phil has one-third the amount of money that Bob has in his account, and Bob has $60 in his account, how much less money does Jenna have in her account than Bob?"""
    # Define Bob's account balance
    bob_balance = 60

    # Calculate Phil's account balance
    phil_balance = bob_balance / 3

    # Calculate Jenna's account balance
    jenna_balance = phil_balance * 2

    # Calculate the difference between Jenna's and Bob's account balances
    difference = bob_balance - jenna_balance

    # return the result
    result = difference
    return result

print(solution())
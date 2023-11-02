def solution():
    """If Jenna has twice as much money in her bank account as Phil does, and Phil has one-third the amount of money that Bob has in his account, and Bob has $60 in his account, how much less money does Jenna have in her account than Bob?"""
    bob_account = 60
    phil_account = bob_account / 3
    jenna_account = 2 * phil_account
    difference = jenna_account - bob_account
    result = difference
    return result

print(solution())
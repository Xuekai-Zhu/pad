def solution():
    """If Jenna has twice as much money in her bank account as Phil does, and Phil has one-third the amount of money that Bob has in his account, and Bob has $60 in his account, how much less money does Jenna have in her account than Bob?"""
    bob_money = 60
    phil_money = bob_money / 3
    jenna_money = phil_money * 2
    difference = bob_money - jenna_money
    result = difference
    return result

print(solution())
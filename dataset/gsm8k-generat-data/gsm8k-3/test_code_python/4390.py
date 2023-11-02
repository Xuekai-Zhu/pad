def solution():
    """If Jenna has twice as much money in her bank account as Phil does, and Phil has one-third the amount of money that Bob has in his account, and Bob has $60 in his account, how much less money does Jenna have in her account than Bob?"""
    # Define the amount of money Bob has in his account
    bob_money = 60

    # Calculate the amount of money that Phil has in his account
    phil_money = bob_money / 3

    # Calculate the amount of money that Jenna has in her account
    jenna_money = 2 * phil_money

    # Calculate how much less money Jenna has than Bob
    less_money = bob_money - jenna_money

    # Display the difference in money
    result = less_money
    return result

print(solution())
def solution():
    """Ian won $100 in the lottery. He decided to use the money to pay off debts. He paid $20 to Colin. He then paid twice as much to Helen, as he had paid to Colin. Then finally, he paid half as much to Benedict, as he had paid to Helen.  How much money, in dollars, does he have left after paying off debts?"""
    # Define the initial amount won in the lottery
    amount_won = 100

    # Define the amount paid to Colin
    paid_to_colin = 20
    amount_left = amount_won - paid_to_colin

    # Define the amount paid to Helen
    paid_to_helen = paid_to_colin * 2
    amount_left -= paid_to_helen

    # Define the amount paid to Benedict
    paid_to_benedict = paid_to_helen / 2
    amount_left -= paid_to_benedict

    # Return the amount of money Ian has left after paying off debts
    result = amount_left
    return result

print(solution())
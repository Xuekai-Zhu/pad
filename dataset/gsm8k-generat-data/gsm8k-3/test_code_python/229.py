def solution():
    """Ian won $100 in the lottery.  He decided to use the money to pay off debts. He paid $20 to Colin. He then paid twice as much to Helen, as he had paid to Colin. Then finally, he paid half as much to Benedict, as he had paid to Helen.  How much money, in dollars, does he have left after paying off debts?"""
    # Define the amount Ian won and the amounts paid to Colin, Helen, and Benedict
    WINNINGS = 100
    COLIN_PAYMENT = 20
    HELEN_PAYMENT = COLIN_PAYMENT * 2
    BENEDICT_PAYMENT = HELEN_PAYMENT / 2

    # Calculate how much money Ian has left
    total_payments = COLIN_PAYMENT + HELEN_PAYMENT + BENEDICT_PAYMENT
    remaining_money = WINNINGS - total_payments

    # Display the remaining money
    result = remaining_money
    return result

print(solution())
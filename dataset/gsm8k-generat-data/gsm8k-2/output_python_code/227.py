def solution():
    """Ian won $100 in the lottery. He decided to use the money to pay off debts. He paid $20 to Colin. He then paid twice as much to Helen, as he had paid to Colin. Then finally, he paid half as much to Benedict, as he had paid to Helen. How much money, in dollars, does he have left after paying off debts?"""
    total_money = 100
    colin_paid = 20
    helen_paid = 2 * colin_paid
    benedict_paid = helen_paid / 2
    total_debt_paid = colin_paid + helen_paid + benedict_paid
    money_left = total_money - total_debt_paid
    result = money_left
    return result

print(solution())
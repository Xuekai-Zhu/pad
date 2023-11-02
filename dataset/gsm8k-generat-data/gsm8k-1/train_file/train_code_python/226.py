def solution():
    """Ian won $100 in the lottery. He decided to use the money to pay off debts. He paid $20 to Colin. He then paid twice as much to Helen, as he had paid to Colin. Then finally, he paid half as much to Benedict, as he had paid to Helen. How much money, in dollars, does he have left after paying off debts?"""
    initial_money = 100
    colin_debt = 20
    helen_debt = 2 * colin_debt
    benedict_debt = helen_debt / 2
    total_debt = colin_debt + helen_debt + benedict_debt
    remaining_money = initial_money - total_debt
    result = remaining_money
    return result

print(solution())
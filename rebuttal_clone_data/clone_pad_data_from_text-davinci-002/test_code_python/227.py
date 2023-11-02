def solution():
    """Ian won $100 in the lottery. He decided to use the money to pay off debts. He paid $20 to Colin. He then paid twice as much to Helen, as he had paid to Colin. Then finally, he paid half as much to Benedict, as he had paid to Helen. How much money, in dollars, does he have left after paying off debts?"""
    initial_money = 100
    money_paid_to_colin = 20
    money_paid_to_helen = money_paid_to_colin * 2
    money_paid_to_benedict = money_paid_to_helen / 2
    total_money_paid = money_paid_to_colin + money_paid_to_helen + money_paid_to_benedict
    money_left = initial_money - total_money_paid
    result = money_left
    
    return result

print(solution())
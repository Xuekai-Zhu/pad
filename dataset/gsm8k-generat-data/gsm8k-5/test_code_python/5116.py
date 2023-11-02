def solution():
    lottery_amount = 12006  # Marge won $12006 in the lottery
    taxes = lottery_amount / 2  # Marge paid half of her winnings for taxes
    remaining_money = lottery_amount - taxes  # Marge has the remaining amount after paying taxes
    loan_payments = remaining_money / 3  # Marge put a third of the leftover money towards her student loans
    savings = 1000  # Marge put $1000 in savings
    investment = savings / 5  # Marge invested a fifth of her savings in the stock market
    fun_money = remaining_money - loan_payments - savings - investment  # Marge has this much money left for fun
    result = fun_money
    return result

print(solution())
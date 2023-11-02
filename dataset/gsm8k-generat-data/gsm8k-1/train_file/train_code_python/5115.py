def solution():
    """Marge had a winning lottery ticket for $12006 and wanted to spend some of it wisely before using on any fun things. 
    She paid half of the lottery amount for the taxes on her winnings, then put a third of the leftover money towards her student loans. 
    She put $1000 in savings and invested a fifth of that amount in the stock market. 
    How many dollars does she have left for fun?"""
    lottery_winnings = 12006
    tax_payment = lottery_winnings / 2
    leftover_money = lottery_winnings - tax_payment
    student_loan_payment = leftover_money / 3
    total_spent = tax_payment + student_loan_payment + 1000
    investment = 1000 / 5
    money_left_for_fun = lottery_winnings - total_spent - investment
    result = money_left_for_fun
    return result

print(solution())
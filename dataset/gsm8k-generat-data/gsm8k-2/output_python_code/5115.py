def solution():
    """Marge had a winning lottery ticket for $12006 and wanted to spend some of it wisely before using on any fun things.
    She paid half of the lottery amount for the taxes on her winnings, then put a third of the leftover money towards her student loans.
    She put $1000 in savings and invested a fifth of that amount in the stock market.
    How many dollars does she have left for fun?"""
    lottery_amount = 12006
    tax_amount = lottery_amount / 2
    leftover_money = lottery_amount - tax_amount
    student_loan_amount = leftover_money / 3
    money_in_savings = 1000
    stock_market_amount = money_in_savings / 5
    remaining_money_for_fun = leftover_money - student_loan_amount - money_in_savings - stock_market_amount
    result = remaining_money_for_fun
    return result

print(solution())
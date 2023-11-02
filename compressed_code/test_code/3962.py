def solution():
    
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
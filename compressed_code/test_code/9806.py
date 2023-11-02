def solution():
    
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
def solution():
    lottery_amount = 12006
    taxes = lottery_amount / 2
    student_loans = (lottery_amount - taxes) / 3
    savings = 1000
    stock_market = savings / 5
    fun_money = lottery_amount - taxes - student_loans - savings - stock_market
    result = fun_money
    return result

print(solution())
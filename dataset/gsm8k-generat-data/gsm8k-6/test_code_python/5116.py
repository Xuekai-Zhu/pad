def solution():
    # Calculate the amount of money Marge has left for fun
    lottery_amount = 12006
    taxes = lottery_amount / 2
    leftover_money = lottery_amount - taxes
    student_loans = leftover_money / 3
    leftover_money -= student_loans
    savings = 1000
    stock_market = savings / 5
    leftover_money -= stock_market
    result = leftover_money
    return result

print(solution())
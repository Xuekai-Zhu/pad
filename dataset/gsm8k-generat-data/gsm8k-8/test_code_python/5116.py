def solution():
    # Calculate the amount paid for taxes
    tax_amount = 12006 / 2

    # Calculate the leftover amount after taxes
    leftover_amount = 12006 - tax_amount

    # Calculate the amount put towards student loans
    loan_amount = leftover_amount / 3

    # Calculate the amount remaining after paying taxes and loans
    remaining_amount = leftover_amount - loan_amount

    # Calculate the amount invested in the stock market
    stock_amount = 1000 / 5

    # Calculate the amount left for fun
    fun_amount = remaining_amount - stock_amount
    result = fun_amount
    return result

print(solution())
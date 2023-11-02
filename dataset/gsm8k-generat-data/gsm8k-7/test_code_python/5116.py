def solution():
    lottery_winnings = 12006

    # Calculate the amount Marge paid for taxes
    taxes = lottery_winnings / 2

    # Calculate the amount of money left after paying taxes
    after_taxes = lottery_winnings - taxes

    # Calculate the amount of money Marge put towards her student loans
    loan_payment = after_taxes / 3

    # Calculate the amount of money Marge put in savings
    savings = 1000

    # Calculate the amount of money Marge invested in the stock market
    stock_investment = savings / 5

    # Calculate the total amount of money spent on taxes, loan payment, savings, and stock investment
    total_spent = taxes + loan_payment + savings + stock_investment

    # Calculate the amount of money Marge has left for fun
    remaining_money = lottery_winnings - total_spent
    result = remaining_money
    return result

print(solution())
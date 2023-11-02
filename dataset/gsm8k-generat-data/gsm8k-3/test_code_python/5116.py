def solution():
    """Marge had a winning lottery ticket for $12006 and wanted to spend some of it wisely before using on any fun things. She paid half of the lottery amount for the taxes on her winnings, then put a third of the leftover money towards her student loans. She put $1000 in savings and invested a fifth of that amount in the stock market. How many dollars does she have left for fun?"""
    # Define the amount of Marge's lottery winnings
    lottery_winnings = 12006

    # Calculate the amount paid for taxes on the winnings
    taxes = lottery_winnings / 2

    # Calculate the amount left after paying taxes
    remaining_money = lottery_winnings - taxes

    # Calculate the amount put towards student loans
    student_loans = remaining_money / 3

    # Calculate the amount put in savings
    savings = 1000

    # Calculate the amount invested in the stock market
    stock_market = savings / 5

    # Calculate the total amount spent wisely
    total_wise_spending = taxes + student_loans + savings + stock_market

    # Calculate the amount left for fun
    amount_left_for_fun = lottery_winnings - total_wise_spending

    # Display the amount left for fun
    result = amount_left_for_fun
    return result

print(solution())
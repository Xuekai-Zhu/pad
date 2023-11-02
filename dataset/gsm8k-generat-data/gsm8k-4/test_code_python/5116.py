def solution():
    """Marge had a winning lottery ticket for $12006 and wanted to spend some of it wisely before using on any fun things. She paid half of the lottery amount for the taxes on her winnings, then put a third of the leftover money towards her student loans. She put $1000 in savings and invested a fifth of that amount in the stock market. How many dollars does she have left for fun?"""
    # Define the initial amount from the lottery
    lottery_amount = 12006

    # Calculate the amount paid for taxes
    tax_amount = lottery_amount / 2

    # Calculate the remaining amount after taxes
    remaining_amount = lottery_amount - tax_amount

    # Calculate the amount put towards student loans
    loan_amount = remaining_amount / 3

    # Calculate the amount put in savings
    savings_amount = 1000

    # Calculate the amount invested in the stock market
    stock_amount = savings_amount / 5

    # Calculate the total amount spent wisely
    wisely_spent = tax_amount + loan_amount + savings_amount + stock_amount

    # Calculate the amount left for fun
    fun_amount = lottery_amount - wisely_spent

    # return the result
    result = fun_amount
    return result

print(solution())
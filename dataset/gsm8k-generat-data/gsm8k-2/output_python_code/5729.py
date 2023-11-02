def solution():
    """Chip has a $50.00 balance on his credit card. Since he didn't pay it off, he will be charged a 20% interest fee. 
    He puts $20.00 on his credit card the following month and doesn't make any payments to his debt. 
    He is hit with another 20% interest fee. What's the current balance on his credit card?"""
    initial_balance = 50
    first_interest = initial_balance * 0.2
    first_balance = initial_balance + first_interest

    second_balance = first_balance + 20
    second_interest = second_balance * 0.2
    final_balance = second_balance + second_interest

    result = final_balance
    return result

print(solution())
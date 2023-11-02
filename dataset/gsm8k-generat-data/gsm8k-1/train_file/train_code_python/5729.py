def solution():
    """Chip has a $50.00 balance on his credit card. Since he didn't pay it off, he will be charged a 20% interest fee. He puts $20.00 on his credit card the following month and doesn't make any payments to his debt. He is hit with another 20% interest fee. What's the current balance on his credit card?"""
    initial_balance = 50
    interest_rate = 20
    first_month_interest = (initial_balance + 20) * (interest_rate / 100)
    first_month_balance = initial_balance + 20 + first_month_interest
    second_month_interest = first_month_balance * (interest_rate / 100)
    final_balance = first_month_balance + second_month_interest
    result = final_balance
    return result

print(solution())
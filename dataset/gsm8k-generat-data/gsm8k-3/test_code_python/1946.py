def solution():
    """Randy has $200 in his piggy bank. He spends 2 dollars every time he goes to the store. He makes 4 trips to the store every month. How much money, in dollars, will be in his piggy bank after a year?"""
    # Define the initial amount in Randy's piggy bank
    initial_amount = 200

    # Define the amount spent each month
    monthly_spending = 2 * 4  # Randy spends $2 per store visit and goes to the store 4 times a month

    # Calculate Randy's ending piggy bank balance after a year
    ending_balance = initial_amount - (monthly_spending * 12)

    # Display the ending balance
    result = ending_balance
    return result

print(solution())
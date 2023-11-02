def solution():
    """George donated half his monthly income to charity and spent $20 from the other half on groceries.
    If he now has $100 left, how much was his monthly income?"""
    
    # Define the amount spent on groceries
    groceries = 20
    
    # Define the amount left after groceries
    after_groceries = 100 + groceries
    
    # Define the total amount, which is twice the amount left after donating to charity
    total = after_groceries * 2
    
    # Define the monthly income, which is the total amount divided by the percentage donated to charity
    income = total / 50
    
    result = income
    return result

print(solution())
def solution():
    """Mary does her grocery shopping on Saturday. She does her shopping only at a specific store where she is allowed a credit of $100, which must be paid in full before her next shopping trip. That week she spent the full credit limit and paid $15 of it on Tuesday and $23 of it on Thursday. How much credit will Mary need to pay before her next shopping trip?"""
    # Define the credit limit and the amounts paid
    credit_limit = 100
    tuesday_payment = 15
    thursday_payment = 23

    # Calculate the remaining credit balance
    remaining_credit = credit_limit - tuesday_payment - thursday_payment

    result = remaining_credit
    return result

print(solution())
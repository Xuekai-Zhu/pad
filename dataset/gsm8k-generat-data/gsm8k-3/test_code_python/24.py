def solution():
    """Mary does her grocery shopping on Saturday. She does her shopping only at a specific store where she is allowed a credit of $100, which must be paid in full before her next shopping trip. That week she spent the full credit limit and paid $15 of it on Tuesday and $23 of it on Thursday. How much credit will Mary need to pay before her next shopping trip?"""
    # Define the credit limit
    credit_limit = 100

    # Calculate the remaining balance after the first payment
    first_payment = 15
    remaining_balance = credit_limit - first_payment

    # Calculate the remaining balance after the second payment
    second_payment = 23
    remaining_balance -= second_payment

    # Calculate the amount of credit that needs to be paid before the next shopping trip
    payment_due = remaining_balance

    result = payment_due
    return result

print(solution())
def solution():
    credit_limit = 100
    amount_paid_on_tuesday = 15
    amount_paid_on_thursday = 23

    # Calculate the total amount spent by Mary
    total_spent = credit_limit - (amount_paid_on_tuesday + amount_paid_on_thursday)

    # Calculate the amount remaining on the credit balance
    credit_remaining = credit_limit - total_spent
    result = credit_remaining
    return result

print(solution())
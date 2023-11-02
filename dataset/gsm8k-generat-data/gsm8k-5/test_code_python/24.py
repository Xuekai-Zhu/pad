def solution():
    credit_limit = 100  # Mary has a credit limit of $100
    amount_spent = credit_limit  # Mary spent the full credit limit
    amount_paid_tuesday = 15  # Mary paid $15 on Tuesday
    amount_paid_thursday = 23  # Mary paid $23 on Thursday

    # Calculate the remaining amount to be paid
    remaining_amount = amount_spent - amount_paid_tuesday - amount_paid_thursday

    result = remaining_amount
    return result

print(solution())
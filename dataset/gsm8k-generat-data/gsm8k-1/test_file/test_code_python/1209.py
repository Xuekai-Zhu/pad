def solution():
    """Stephen borrowed $300 from his sister and promised to return it with an additional 2% of the money he owed. For 11 months Stephen will give his sister $25 per month and the remaining amount, including the interest, will be paid on the twelfth month. How much will Stephen pay in the twelfth month?"""
    borrowed_amount = 300
    interest_rate = 0.02
    remaining_amount = borrowed_amount * (1 + interest_rate)
    remaining_months = 1
    monthly_payment = 25
    total_paid = monthly_payment * 11
    final_payment = remaining_amount - total_paid
    result = final_payment
    return result

print(solution())
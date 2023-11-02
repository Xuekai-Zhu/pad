def solution():
    """Isabelle’s parents bought a new television for $480. The seller gives them a 5% discount. They pay a first installment of $150 and will pay the rest in 3 monthly installments. What is the amount of a monthly payment?"""
    tv_price = 480
    discount = tv_price * 0.05
    discounted_price = tv_price - discount
    remaining_amount = discounted_price - 150
    monthly_installments = 3
    monthly_payment = remaining_amount / monthly_installments
    result = monthly_payment
    return result

print(solution())
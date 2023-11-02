def solution():
    """Isabelle’s parents bought a new television for $480. The seller gives them a 5% discount. They pay a first installment of $150 and will pay the rest in 3 monthly installments. What is the amount of a monthly payment?"""
    initial_price = 480
    discount_percent = 5
    discount_amount = initial_price * (discount_percent / 100)
    discounted_price = initial_price - discount_amount
    remaining_balance = discounted_price - 150
    num_installments = 3
    monthly_payment = remaining_balance / num_installments
    result = monthly_payment
    return result

print(solution())
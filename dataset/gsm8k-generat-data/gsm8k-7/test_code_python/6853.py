def solution():
    original_price = 480
    discount_rate = 0.05  # 5% discount
    discounted_price = original_price * (1 - discount_rate)
    first_payment = 150
    remaining_balance = discounted_price - first_payment
    num_installments = 3

    # Calculate the amount of each monthly installment
    monthly_payment = remaining_balance / num_installments
    result = monthly_payment
    return result

print(solution())
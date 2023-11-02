def solution():
    original_price = 480  # The TV's original price is $480
    discount_rate = 0.05  # The seller gives a 5% discount
    discounted_price = original_price * (1 - discount_rate)  # The discounted price after the discount is applied
    remaining_amount = discounted_price - 150  # The amount remaining to be paid after the first installment of $150

    # Calculate the monthly payment amount
    monthly_payment = remaining_amount / 3
    result = monthly_payment
    return result

print(solution())
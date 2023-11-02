def solution():
    discount_percent = 25  # Maria received a 25% discount
    discount_amount = 40  # The discount she received was $40

    # Calculate the original price before the discount
    original_price = discount_amount / (discount_percent/100)

    # Calculate the total amount Maria paid after the discount
    total_amount_paid = original_price - discount_amount
    result = total_amount_paid
    return result

print(solution())
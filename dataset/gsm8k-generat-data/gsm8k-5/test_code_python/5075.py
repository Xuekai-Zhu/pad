def solution():
    purchase_amount = 250  # The original purchase amount is $250
    discount_denominator = 100  # The discount is applied for every $100 spent
    discount_amount = (purchase_amount // discount_denominator) * 10  # Calculate the discount amount

    # Calculate the final amount paid after the discount
    final_amount = purchase_amount - discount_amount
    result = final_amount
    return result

print(solution())
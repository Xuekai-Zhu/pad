def solution():
    price_per_person = 25.00  # Monica charges $25.00 per person
    repeat_customer_discount = 0.10  # Monica offers a 10% discount for repeat customers
    num_guests = 20  # Phoebe is having a dinner party for 20 guests

    # Calculate the total price before the discount
    total_price = price_per_person * num_guests

    # Calculate the discount amount
    discount_amount = repeat_customer_discount * total_price

    # Calculate the total price after the discount
    total_price_after_discount = total_price - discount_amount

    result = total_price_after_discount
    return result

print(solution())
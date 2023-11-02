def solution():
    book1_price = 13.00
    book2_price = 15.00
    book3_price = 10.00
    book4_price = 10.00
    num_books = 4
    discount = 0.25  # 25% off for first two books
    free_shipping_threshold = 50.00

    # Calculate the total cost of the first four books before discount
    total_cost_before_discount = (book1_price + book2_price) + (book3_price + book4_price)

    # Calculate the cost of the first two books after discount
    discounted_cost = (book1_price + book2_price) * (1 - discount)

    # Calculate the total cost of all four books after discount
    total_cost_after_discount = discounted_cost + (book3_price + book4_price)

    # Calculate the amount needed to reach the free shipping threshold
    additional_amount_needed = free_shipping_threshold - total_cost_after_discount

    if additional_amount_needed <= 0:
        result = 0
    else:
        result = additional_amount_needed
    return result

print(solution())
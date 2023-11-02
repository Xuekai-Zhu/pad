def solution():
    original_price = 12  # Original price of one Uno Giant Family Card
    discount = 2  # Discount given on each card when buying 10 or more
    quantity = 10  # Number of cards bought by Ivan

    # Calculate the discounted price per card
    discounted_price = original_price - discount

    # Calculate the total amount paid by Ivan
    total_amount = discounted_price * quantity
    result = total_amount
    return result

print(solution())
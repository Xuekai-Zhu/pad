def solution():
    suit_price = 430  # Suit price
    shoes_price = 190  # Shoes price
    discount = 100  # Discount received by the customer

    # Calculate the total amount before discount
    total_amount = suit_price + shoes_price

    # Calculate the final amount to be paid after discount
    final_amount = total_amount - discount
    result = final_amount
    return result

print(solution())
def solution():
    """A department store displays a 20% discount on all fixtures. What will be the new price of a 25 cm high bedside lamp that was worth $120?"""
    # Define the original price of the bedside lamp
    original_price = 120

    # Define the discount percentage
    discount_percentage = 20

    # Calculate the discount amount
    discount_amount = original_price * (discount_percentage / 100)

    # Calculate the new price of the bedside lamp after the discount
    new_price = original_price - discount_amount

    # Display the new price of the bedside lamp
    result = new_price
    return result

print(solution())
def solution():
    """A department store displays a 20% discount on all fixtures. What will be the new price of a 25 cm high bedside lamp that was worth $120?"""
    # Define the original price and the discount percentage
    original_price = 120
    discount_percentage = 0.2

    # Calculate the discount amount
    discount_amount = original_price * discount_percentage

    # Calculate the new price after the discount
    new_price = original_price - discount_amount

    result = new_price
    return result

print(solution())
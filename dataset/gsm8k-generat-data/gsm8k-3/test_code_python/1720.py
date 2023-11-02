def solution():
    """Lyra bought a pair of shoes at a 20% discount.  If she paid $480, how much was the original price of the pair of shoes?"""
    # Define the price Lyra paid and the discount percentage
    price_paid = 480
    discount_percentage = 20

    # Calculate the original price of the shoes
    original_price = price_paid / (1 - discount_percentage/100)

    # Display the original price
    result = original_price
    return result

print(solution())
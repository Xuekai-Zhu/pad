def solution():
    """Rose bought a plant with a 10% discount. If the price is $10, how much did Rose pay after the discount?"""
    # Define the original price and discount percentage
    original_price = 10
    discount_percentage = 0.1

    # Calculate the discount amount
    discount_amount = original_price * discount_percentage

    # Calculate the discounted price
    discounted_price = original_price - discount_amount

    # Display the discounted price
    result = discounted_price
    return result

print(solution())
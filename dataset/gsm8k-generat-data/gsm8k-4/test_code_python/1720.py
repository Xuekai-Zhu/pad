def solution():
    """Lyra bought a pair of shoes at a 20% discount. If she paid $480, how much was the original price of the pair of shoes?"""
    # Define the discounted price and the discount percentage
    discounted_price = 480
    discount_percentage = 0.20

    # Calculate the original price
    original_price = discounted_price / (1 - discount_percentage)

    result = original_price
    return result

print(solution())
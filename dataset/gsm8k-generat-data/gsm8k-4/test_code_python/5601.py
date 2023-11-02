def solution():
    """Macy's is selling shirts that have been reduced to $6. This price is at 25% of the original price. What was the original price?"""
    # Define the current price and the discount percentage
    current_price = 6
    discount = 0.25

    # Calculate the original price using the formula: original_price = current_price / (1 - discount)
    original_price = current_price / (1 - discount)

    result = original_price
    return result

print(solution())
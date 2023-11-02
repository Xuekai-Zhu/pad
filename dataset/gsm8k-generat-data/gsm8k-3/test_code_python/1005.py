def solution():
    """4 friends went to buy from a clothes shop. Every item was 50% off.  All four friends decided to buy a t-shirt. The original price of the t-shirt was 20 dollars. How much money did they spend in total?"""
    # Define the original price of the t-shirt
    ORIGINAL_PRICE = 20

    # Calculate the discounted price of the t-shirt
    DISCOUNTED_PRICE = ORIGINAL_PRICE * 0.5

    # Calculate the total amount spent by all four friends
    total_spent = DISCOUNTED_PRICE * 4

    # Display the total amount spent
    result = total_spent
    return result

print(solution())
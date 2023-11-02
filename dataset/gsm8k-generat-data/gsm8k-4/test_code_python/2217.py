def solution():
    """Mrs. Taylor bought two smart televisions that cost $650 each. If the total sales price had a 25% discount, how much did Mrs. Taylor pay for the two televisions?"""
    # Define the original price of one television
    original_price = 650

    # Calculate the discounted price of one television
    discount = 0.25
    discounted_price = original_price * (1 - discount)

    # Calculate the total cost of two televisions at discounted price
    total_cost = discounted_price * 2

    # return the result
    result = total_cost
    return result

print(solution())
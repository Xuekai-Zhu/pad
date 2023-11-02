def solution():
    """A luxury perfume costs $1200. The store owner decided to increase its price by 10% so that he could earn more profit. Few weeks had past but the perfume was still not sold. So, the owner decided to lower the price by 15%. By how much was the final price lower than the original price?"""
    # Define the original price of the perfume
    original_price = 1200

    # Calculate the price after a 10% increase
    price_after_increase = original_price * 1.1

    # Calculate the price after a 15% decrease from the increased price
    price_after_decrease = price_after_increase * 0.85

    # Calculate the difference between the original price and the final price
    price_difference = original_price - price_after_decrease

    result = price_difference
    return result

print(solution())
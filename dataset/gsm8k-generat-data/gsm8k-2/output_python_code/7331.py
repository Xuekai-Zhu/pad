def solution():
    """John decides to start collecting art. He pays the same price for his first 3 pieces of art and the total price came to $45,000. The next piece of art was 50% more expensive than those. How much did all the art cost?"""
    first_three_price = 45000 / 3
    next_price = 1.5 * first_three_price
    total_price = 4 * next_price
    result = total_price
    return result

print(solution())
def solution():
    """4 friends went to buy from a clothes shop. Every item was 50% off. All four friends decided to buy a t-shirt. The original price of the t-shirt was 20 dollars. How much money did they spend in total?"""
    original_price = 20
    discount = 50
    discounted_price = original_price - (original_price * (discount / 100))
    total_price = discounted_price * 4
    result = total_price
    return result

print(solution())
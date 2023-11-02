def solution():
    """Martin went to a store to buy a new television set. He decided to spend no more than $1,000 and the sales clerk offered him the TV for $100 less and an additional 20% off. How much lower was the price of the television than the amount Martin decided to spend?"""
    max_price = 1000
    discounted_price = (max_price - 100) * 0.8
    price_difference = max_price - discounted_price
    result = price_difference
    return result

print(solution())
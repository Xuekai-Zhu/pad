def solution():
    """Martin went to a store to buy a new television set. He decided to spend no more than $1,000 and the sales clerk offered him the TV for $100 less and an additional 20% off. How much lower was the price of the television than the amount Martin decided to spend?"""
    # Define the maximum amount Martin decided to spend
    MAX_SPEND = 1000

    # Calculate the original price of the TV
    original_price = MAX_SPEND + 100

    # Calculate the discounted price of the TV
    discounted_price = original_price * 0.8

    # Calculate how much lower the price of the TV is than the maximum amount Martin decided to spend
    price_difference = MAX_SPEND - discounted_price

    # Display the price difference
    result = price_difference
    return result

print(solution())
def solution():
    """Martin went to a store to buy a new television set. He decided to spend no more than $1,000 and the sales clerk offered him the TV for $100 less and an additional 20% off. How much lower was the price of the television than the amount Martin decided to spend?"""
    # Define the maximum amount Martin will spend
    max_amount = 1000

    # Define the original price of the TV
    original_price = None

    # Define the final price of the TV after discounts
    final_price = None

    # Define the difference between the final price and the maximum amount Martin will spend
    price_difference = None

    # Calculate the original price of the TV
    original_price = max_amount + 100

    # Calculate the final price of the TV after discounts
    final_price = original_price * 0.8

    # Calculate the difference between the final price and the maximum amount Martin will spend
    price_difference = max_amount - final_price

    # return the result
    result = price_difference
    return result

print(solution())
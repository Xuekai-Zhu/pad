def solution():
    """One necklace is worth $34. Bob decided to buy one for his wife. But, he also bought a book, which is $5 more expensive than the necklace. Before he went shopping, Bob set a limit and decided not to spend more than $70. How many dollars over the "limit" did Bob spend?"""
    # Define the price of the necklace and the book
    necklace_price = 34
    book_price = necklace_price + 5

    # Define the spending limit
    spending_limit = 70

    # Calculate the total spent
    total_spent = necklace_price + book_price

    # Calculate the amount spent over the limit
    amount_over_limit = total_spent - spending_limit

    # Return the result
    result = amount_over_limit
    return result

print(solution())
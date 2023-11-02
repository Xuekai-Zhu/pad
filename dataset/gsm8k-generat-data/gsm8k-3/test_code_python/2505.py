def solution():
    """One necklace is worth $34. Bob decided to buy one for his wife. But, he also bought a book, which is $5 more expensive than the necklace. Before he went shopping, Bob set a limit and decided not to spend more than $70. How many dollars over the "limit" did Bob spend?"""
    # Define the cost of the necklace and book
    NECKLACE_COST = 34
    BOOK_COST = NECKLACE_COST + 5

    # Define the spending limit
    SPENDING_LIMIT = 70

    # Calculate the total cost of the necklace and book
    total_cost = NECKLACE_COST + BOOK_COST

    # Calculate the amount Bob spent over the spending limit
    over_limit = total_cost - SPENDING_LIMIT

    # Display the amount Bob spent over the limit
    result = over_limit
    return result

print(solution())
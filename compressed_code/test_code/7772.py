def solution():
    """
    One necklace is worth $34. Bob decided to buy one for his wife. But, he also bought a book, which is $5 more expensive than the necklace. Before he went shopping, Bob set a limit and decided not to spend more than $70. How many dollars over the "limit" did Bob spend?
    """
    necklace_cost = 34
    book_cost = necklace_cost + 5
    total_cost = necklace_cost + book_cost
    limit = 70
    over_limit = total_cost - limit
    result = over_limit
    return result

print(solution())
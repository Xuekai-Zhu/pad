def solution():
    """A clothing store sells 20 shirts and 10 pairs of jeans. A shirt costs $10 each and a pair of jeans costs twice as much. How much will the clothing store earn if all shirts and jeans are sold?"""
    # Define the prices of shirts and jeans
    shirt_price = 10
    jeans_price = 2 * shirt_price

    # Calculate the total earnings from selling shirts
    shirt_earnings = shirt_price * 20

    # Calculate the total earnings from selling jeans
    jeans_earnings = jeans_price * 10

    # Calculate the total earnings from selling all items
    total_earnings = shirt_earnings + jeans_earnings

    # return the result
    result = total_earnings
    return result

print(solution())
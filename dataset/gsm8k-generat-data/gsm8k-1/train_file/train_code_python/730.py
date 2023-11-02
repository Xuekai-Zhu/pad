def solution():
    """A clothing store sells 20 shirts and 10 pairs of jeans. A shirt costs $10 each and a pair of jeans costs twice as much. How much will the clothing store earn if all shirts and jeans are sold?"""
    shirts_sold = 20
    jeans_sold = 10
    shirt_price = 10
    jeans_price = 2 * shirt_price
    total_earned = (shirts_sold * shirt_price) + (jeans_sold * jeans_price)
    result = total_earned
    return result

print(solution())
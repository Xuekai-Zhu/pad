def solution():
    """A clothing store sells 20 shirts and 10 pairs of jeans. A shirt costs $10 each and a pair of jeans costs twice as much. How much will the clothing store earn if all shirts and jeans are sold?"""
    shirt_price = 10
    jeans_price = 2 * shirt_price
    total_shirt_price = 20 * shirt_price
    total_jeans_price = 10 * jeans_price
    total_earnings = total_shirt_price + total_jeans_price
    result = total_earnings
    return result

print(solution())
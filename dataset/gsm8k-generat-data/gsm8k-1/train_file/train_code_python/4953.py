def solution():
    """Jangshe spent $610 on 7 pieces of clothing. One piece was $49 and another piece was $81. If the other pieces were all the same price, how many dollars was one of the other pieces?"""
    total_cost = 610
    known_prices = [49, 81]
    num_unknown_prices = 5
    unknown_price = (total_cost - sum(known_prices)) / num_unknown_prices
    result = unknown_price
    return result

print(solution())
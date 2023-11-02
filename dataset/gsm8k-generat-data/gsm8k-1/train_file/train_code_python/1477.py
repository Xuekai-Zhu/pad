def solution():
    """John bought a tennis racket. He also bought sneakers that cost $200 and a sports outfit that cost $250. He spent a total of $750 for all those items. What was the price of the racket?"""
    total_cost = 750
    sneaker_cost = 200
    outfit_cost = 250
    racket_cost = total_cost - sneaker_cost - outfit_cost
    result = racket_cost
    return result

print(solution())
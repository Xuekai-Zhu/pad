def solution():
    """John bought a tennis racket. He also bought sneakers that cost $200 and a sports outfit that cost $250. He spent a total of $750 for all those items. What was the price of the racket?"""
    total_spent = 750
    sneakers_price = 200
    sports_outfit_price = 250
    racket_price = total_spent - sneakers_price - sports_outfit_price
    result = racket_price
    return result

print(solution())
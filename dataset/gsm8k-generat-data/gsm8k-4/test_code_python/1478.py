def solution():
    """John bought a tennis racket. He also bought sneakers that cost $200 and a sports outfit that cost $250. He spent a total of $750 for all those items. What was the price of the racket?"""
    # Define the prices of the shoes and outfit
    shoes_price = 200
    outfit_price = 250

    # Calculate the total cost of the shoes and outfit
    total_cost = shoes_price + outfit_price

    # Calculate the price of the tennis racket
    racket_price = 750 - total_cost

    # Return the price of the tennis racket
    result = racket_price
    return result

print(solution())
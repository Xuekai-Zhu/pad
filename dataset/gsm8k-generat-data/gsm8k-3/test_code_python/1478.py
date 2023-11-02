def solution():
    """John bought a tennis racket. He also bought sneakers that cost $200 and a sports outfit that cost $250. He spent a total of $750 for all those items. What was the price of the racket?"""
    # Define the prices of the sneakers and sports outfit
    SNEAKERS_PRICE = 200
    OUTFIT_PRICE = 250

    # Calculate the total cost of the sneakers and sports outfit
    total_accessory_cost = SNEAKERS_PRICE + OUTFIT_PRICE

    # Calculate the cost of the tennis racket
    racket_cost = 750 - total_accessory_cost

    # Display the cost of the tennis racket
    result = racket_cost
    return result

print(solution())
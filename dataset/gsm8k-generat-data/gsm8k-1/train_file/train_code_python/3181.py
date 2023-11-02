def solution():
    """Mrs. Brynlee reduced the prices of items in her store by 20% after the local government gave small businesses in her county a subsidy. If the price of a shirt in the store was $60 and that of the leather jacket was $90, calculate the amount of money Teagan will pay for buying 5 shirts and 10 leather jackets at the reduced prices."""
    new_price_shirt = 60 * 0.8
    new_price_jacket = 90 * 0.8
    total_cost = (new_price_shirt * 5) + (new_price_jacket * 10)
    result = total_cost
    return result

print(solution())
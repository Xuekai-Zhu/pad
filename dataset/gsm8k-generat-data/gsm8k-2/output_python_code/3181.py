def solution():
    """Mrs. Brynlee reduced the prices of items in her store by 20% after the local government gave small businesses in her county a subsidy. If the price of a shirt in the store was $60 and that of the leather jacket was $90, calculate the amount of money Teagan will pay for buying 5 shirts and 10 leather jackets at the reduced prices."""
    shirt_price = 60
    jacket_price = 90
    discount = 0.2
    discount_shirt_price = shirt_price - (shirt_price * discount)
    discount_jacket_price = jacket_price - (jacket_price * discount)
    total_cost = (5 * discount_shirt_price) + (10 * discount_jacket_price)
    result = total_cost
    return result

print(solution())
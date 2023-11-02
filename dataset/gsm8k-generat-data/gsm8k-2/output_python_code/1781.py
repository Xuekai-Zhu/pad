def solution():
    """In a restaurant, a burger costs $9, and a pizza twice as much. How much would cost one pizza and three burgers?"""
    burger_price = 9
    pizza_price = 2 * burger_price
    total_price = pizza_price + (3 * burger_price)
    result = total_price
    return result

print(solution())
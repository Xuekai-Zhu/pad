def solution():
    """In a restaurant, a burger costs $9, and a pizza twice as much. How much would cost one pizza and three burgers?"""
    burger_price = 9
    pizza_price = burger_price * 2
    total_cost = (3 * burger_price) + pizza_price
    result = total_cost
    return result

print(solution())
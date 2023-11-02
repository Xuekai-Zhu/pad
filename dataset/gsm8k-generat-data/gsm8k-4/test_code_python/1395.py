def solution():
    """Mike bought a DVD of his favorite movie. He paid $5 for it at the store. A friend of Mike's, Steve, saw this and also decided to buy a DVD of the movie, but it was already sold out. He needed to order it online, which cost him twice as much. And in addition, he needed to pay the shipping costs which were 80% of the price of the film he ordered. How much did Steve pay to get the DVD in total?"""
    # Define the initial cost of the DVD and the cost of ordering it online
    INITIAL_COST = 5
    ONLINE_COST = INITIAL_COST * 2

    # Calculate the shipping cost
    shipping_cost = ONLINE_COST * 0.8

    # Calculate the total cost
    total_cost = ONLINE_COST + shipping_cost

    result = total_cost
    return result

print(solution())
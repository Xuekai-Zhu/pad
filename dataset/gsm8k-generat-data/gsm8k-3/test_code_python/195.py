def solution():
    """Mary bought 5 boxes of drinks at $6 each box and 10 boxes of pizzas at $14 each box for her pizza party. She paid $200 for all the items. How much change did she get back?"""
    # Define the prices and quantities of drinks and pizzas
    drinks_price = 6
    pizzas_price = 14
    drinks_quantity = 5
    pizzas_quantity = 10

    # Calculate the total cost of the items
    total_cost = (drinks_price * drinks_quantity) + (pizzas_price * pizzas_quantity)

    # Calculate the change Mary received
    change = 200 - total_cost

    # return the result
    result = change
    return result

print(solution())
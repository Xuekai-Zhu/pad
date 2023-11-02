def solution():
    """Stefan goes to a restaurant to eat dinner with his family. They order an appetizer that costs $10 and 4 entrees that are $20 each. If they tip 20% of the total for the waiter, what is the total amount of money that they spend at the restaurant?"""
    appetizer_cost = 10
    entree_cost = 20
    num_entrees = 4
    subtotal = appetizer_cost + (entree_cost * num_entrees)
    tip_percent = 20
    tip_amount = subtotal * (tip_percent / 100)
    total_cost = subtotal + tip_amount
    result = total_cost
    return result

print(solution())
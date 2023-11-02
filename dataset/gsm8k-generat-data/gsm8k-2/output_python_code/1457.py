def solution():
    """Stefan goes to a restaurant to eat dinner with his family. They order an appetizer that costs $10 and 4 entrees that are $20 each. If they tip 20% of the total for the waiter, what is the total amount of money that they spend at the restaurant?"""
    appetizer_cost = 10
    entree_cost = 20
    num_entrees = 4
    meal_cost = appetizer_cost + (entree_cost * num_entrees)
    tip_percent = 0.2
    tip_amount = meal_cost * tip_percent
    total_cost = meal_cost + tip_amount
    result = total_cost
    return result

print(solution())
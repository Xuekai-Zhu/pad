def solution():
    """Stefan goes to a restaurant to eat dinner with his family. They order an appetizer that costs $10 and 4 entrees that are $20 each. If they tip 20% of the total for the waiter, what is the total amount of money that they spend at the restaurant?"""
    # Define the cost of the appetizer and entrees
    APPETIZER_COST = 10
    ENTREE_COST = 20

    # Calculate the total cost of the entrees
    entree_total = ENTREE_COST * 4

    # Calculate the subtotal (total cost before tip)
    subtotal = APPETIZER_COST + entree_total

    # Calculate the tip amount
    tip = subtotal * 0.2

    # Calculate the total cost (subtotal plus tip)
    total_cost = subtotal + tip
    
    result = total_cost
    return result

print(solution())
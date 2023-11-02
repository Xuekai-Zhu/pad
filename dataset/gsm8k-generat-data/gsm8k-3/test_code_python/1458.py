def solution():
    """Stefan goes to a restaurant to eat dinner with his family. They order an appetizer that costs $10 and 4 entrees that are $20 each. If they tip 20% of the total for the waiter, what is the total amount of money that they spend at the restaurant?"""
    # Define the cost of the appetizer and entrees
    APPETIZER_COST = 10
    ENTREE_COST = 20

    # Define the number of appetizers and entrees ordered
    num_appetizers = 1
    num_entrees = 4

    # Calculate the total cost of the meal
    meal_cost = (num_appetizers * APPETIZER_COST) + (num_entrees * ENTREE_COST)

    # Calculate the tip for the waiter
    tip_amount = meal_cost * 0.2

    # Calculate the total amount spent at the restaurant
    total_cost = meal_cost + tip_amount

    # Display the total cost
    result = total_cost
    return result

print(solution())
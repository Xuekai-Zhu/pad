def solution():
    """Victoria was given a $50 bill by her mother to buy her friends snacks for their group meeting. She bought 2 boxes of pizza that costs $12 each and 2 packs of juice drinks that cost $2 each. How much money should Victoria return to her mother?"""
    # Define the cost of each item
    PIZZA_COST = 12
    JUICE_COST = 2

    # Define the amount of each item purchased
    pizza_boxes = 2
    juice_packs = 2

    # Calculate the total cost of the pizzas
    pizza_cost = pizza_boxes * PIZZA_COST

    # Calculate the total cost of the juice packs
    juice_cost = juice_packs * JUICE_COST

    # Calculate the total cost of all the snacks
    total_cost = pizza_cost + juice_cost

    # Calculate the amount of change to be returned to Victoria's mother
    change = 50 - total_cost

    # Display the amount of change to be returned
    result = change
    return result

print(solution())
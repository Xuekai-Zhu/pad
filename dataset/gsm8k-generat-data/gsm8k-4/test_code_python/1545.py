def solution():
    """Nina wants to give presents to her children. She buys three toys at $10 each, two packs of basketball cards at $5 each, and five shirts at $6 each. How much does she spend in all?"""
    # Define the prices and quantities of each item
    toys_price = 10
    toys_quantity = 3
    cards_price = 5
    cards_quantity = 2
    shirts_price = 6
    shirts_quantity = 5

    # Calculate the total cost of each item
    total_toys_cost = toys_price * toys_quantity
    total_cards_cost = cards_price * cards_quantity
    total_shirts_cost = shirts_price * shirts_quantity

    # Calculate the total cost of all items
    total_cost = total_toys_cost + total_cards_cost + total_shirts_cost

    # Return the total cost
    result = total_cost
    return result

print(solution())
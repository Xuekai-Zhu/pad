def solution():
    """Nina wants to give presents to her children. She buys three toys at $10 each, two packs of basketball cards at $5 each, and five shirts at $6 each. How much does she spend in all?"""
    # Define the cost of each item
    TOY_COST = 10
    CARD_COST = 5
    SHIRT_COST = 6

    # Define the number of each item purchased
    toy_num = 3
    card_num = 2
    shirt_num = 5

    # Calculate the total cost of the toys
    toy_cost = toy_num * TOY_COST

    # Calculate the total cost of the basketball cards
    card_cost = card_num * CARD_COST

    # Calculate the total cost of the shirts
    shirt_cost = shirt_num * SHIRT_COST

    # Calculate the total cost of all the presents
    total_cost = toy_cost + card_cost + shirt_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())
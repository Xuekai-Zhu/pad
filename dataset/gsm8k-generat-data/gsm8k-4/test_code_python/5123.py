def solution():
    """Olivia bought two packs of basketball cards at $3 each, and 5 decks of baseball cards at $4 each. If she had one $50 bill, how much change did she receive?"""
    # Define the cost of the basketball cards and the number of packs purchased
    basketball_card_cost = 3
    num_basketball_packs = 2

    # Define the cost of the baseball cards and the number of decks purchased
    baseball_card_cost = 4
    num_baseball_decks = 5

    # Calculate the total cost of the purchase
    total_cost = (basketball_card_cost * num_basketball_packs) + (baseball_card_cost * num_baseball_decks)

    # Calculate the change received
    change = 50 - total_cost

    # Return the change received
    result = change
    return result

print(solution())
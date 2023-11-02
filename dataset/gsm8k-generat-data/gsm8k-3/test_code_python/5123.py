def solution():
    """Olivia bought two packs of basketball cards at $3 each, and 5 decks of baseball cards at $4 each.  If she had one $50 bill, how much change did she receive?"""
    # Define the cost of the basketball cards and baseball cards
    BASKETBALL_PRICE = 3
    BASEBALL_PRICE = 4

    # Define the number of packs of basketball cards and decks of baseball cards purchased
    basketball_packs = 2
    baseball_decks = 5

    # Calculate the total cost of the basketball cards
    basketball_cost = basketball_packs * BASKETBALL_PRICE

    # Calculate the total cost of the baseball cards
    baseball_cost = baseball_decks * BASEBALL_PRICE

    # Calculate the total cost of all the cards
    total_cost = basketball_cost + baseball_cost

    # Calculate the change Olivia received
    change = 50 - total_cost
    
    # Display the change Olivia received
    result = change
    return result

print(solution())
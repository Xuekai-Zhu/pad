def solution():
    """Olivia bought two packs of basketball cards at $3 each, and 5 decks of baseball cards at $4 each. If she had one $50 bill, how much change did she receive?"""
    basketball_cards_cost = 3 * 2
    baseball_cards_cost = 4 * 5
    total_cost = basketball_cards_cost + baseball_cards_cost
    change = 50 - total_cost
    result = change
    return result

print(solution())
def solution():
    """Bella has two times as many marbles as frisbees. She also has 20 more frisbees than deck cards. If she buys 2/5 times more of each item, what would be the total number of the items she will have if she currently has 60 marbles?"""
    # Define the current number of marbles and the ratio of marbles to frisbees
    current_marbles = 60
    marble_frisbee_ratio = 2

    # Calculate the current number of frisbees and deck cards
    current_frisbees = current_marbles // marble_frisbee_ratio
    current_deck_cards = current_frisbees - 20

    # Calculate the new quantities of marbles, frisbees, and deck cards
    new_marbles = current_marbles * 2.4
    new_frisbees = (current_frisbees + 20) * 2.4
    new_deck_cards = (current_deck_cards) * 2.4

    # Calculate the total number of items after the purchase
    total_items = new_marbles + new_frisbees + new_deck_cards

    # return the result
    result = total_items
    return result

print(solution())
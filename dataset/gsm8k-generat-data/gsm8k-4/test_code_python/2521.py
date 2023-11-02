def solution():
    """Janet has 9 cards more than Brenda. Mara has twice as many cards as Janet. How many cards do they have in all if Mara has 40 cards less than 150?"""
    # Calculate the number of cards Mara has
    mara_cards = 150 - 40

    # Calculate the number of cards Janet has (9 more than Brenda)
    janet_cards = mara_cards / 2
    brenda_cards = janet_cards - 9

    # Calculate the total number of cards
    total_cards = janet_cards + brenda_cards + mara_cards

    # Return the result
    result = total_cards
    return result

print(solution())
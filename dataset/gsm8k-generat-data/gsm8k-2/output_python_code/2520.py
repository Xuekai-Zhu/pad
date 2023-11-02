def solution():
    """Janet has 9 cards more than Brenda. Mara has twice as many cards as Janet. How many cards do they have in all if Mara has 40 cards less than 150?"""
    mara_cards = 150 - 40
    janet_cards = mara_cards / 2
    brenda_cards = janet_cards - 9
    total_cards = mara_cards + janet_cards + brenda_cards
    result = total_cards
    return result

print(solution())
def solution():
    # Calculate the number of cards Mara has
    mara_cards = 150 - 40

    # Calculate the number of cards Janet has
    janet_cards = mara_cards / 2

    # Calculate the number of cards Brenda has
    brenda_cards = janet_cards - 9

    # Calculate the total number of cards
    total_cards = mara_cards + janet_cards + brenda_cards
    result = total_cards
    return result

print(solution())
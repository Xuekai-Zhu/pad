def solution():
    mara_cards = 150 - 40  # Mara has 40 cards less than 150
    janet_cards = mara_cards / 2  # Janet has half as many cards as Mara
    brenda_cards = janet_cards - 9  # Brenda has 9 cards less than Janet
    total_cards = mara_cards + janet_cards + brenda_cards  # Total number of cards they have

    result = total_cards
    return result

print(solution())
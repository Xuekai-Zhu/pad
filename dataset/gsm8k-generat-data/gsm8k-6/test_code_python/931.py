def solution():
    # Calculate how many cards Malcom has
    malcom_cards = 20 + 8  # Malcom has 8 more cards than Brandon

    # Calculate how many cards Mark has after Malcom gives him half
    mark_cards = malcom_cards / 2

    # Calculate how many cards Malcom has left after giving half to Mark
    malcom_cards_left = malcom_cards - mark_cards
    result = malcom_cards_left
    return result

print(solution())
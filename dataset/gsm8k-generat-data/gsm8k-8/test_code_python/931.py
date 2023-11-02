def solution():
    # Define the number of Brandon's cards and Malcom's cards
    brandon_cards = 20
    malcom_cards = brandon_cards + 8

    # Calculate how many cards Malcom gives to Mark
    cards_to_mark = malcom_cards / 2

    # Calculate how many cards Malcom has left
    malcom_cards_left = malcom_cards - cards_to_mark
    result = malcom_cards_left
    return result

print(solution())
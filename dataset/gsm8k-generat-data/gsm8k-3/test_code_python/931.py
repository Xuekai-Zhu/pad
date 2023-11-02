def solution():
    """Brandon has a collection of 20 baseball cards.  Malcom has 8 more cards than Brandon.  However, then Malcom gives half of his cards to his friend Mark.  How many cards does Malcom have left?"""
    # Define the number of cards Brandon has
    brandon_cards = 20

    # Calculate the number of cards Malcom has
    malcom_cards = brandon_cards + 8

    # Calculate the number of cards Malcom gives to Mark
    cards_given_away = malcom_cards // 2

    # Calculate the number of cards Malcom has left
    cards_left = malcom_cards - cards_given_away

    # Display the number of cards Malcom has left
    result = cards_left
    return result

print(solution())
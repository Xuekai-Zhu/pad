def solution():
    """Brandon has a collection of 20 baseball cards. Malcom has 8 more cards than Brandon. However, then Malcom gives half of his cards to his friend Mark. How many cards does Malcom have left?"""
    brandon_cards = 20
    malcom_cards = brandon_cards + 8
    cards_given = malcom_cards / 2
    malcom_cards_left = malcom_cards - cards_given
    result = malcom_cards_left
    
    return result

print(solution())
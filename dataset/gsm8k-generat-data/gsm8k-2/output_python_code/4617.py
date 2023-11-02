def solution():
    """Dexter filled 3 fewer plastic boxes with football cards than basketball cards. He filled 9 boxes with basketball cards and each box has 15 cards. For the boxes with football cards, he filled each box with 20 cards. How many cards does Dexter have in total?"""
    basketball_boxes = 9
    basketball_cards_per_box = 15
    football_boxes = basketball_boxes - 3
    football_cards_per_box = 20
    total_basketball_cards = basketball_boxes * basketball_cards_per_box
    total_football_cards = football_boxes * football_cards_per_box
    total_cards = total_basketball_cards + total_football_cards
    result = total_cards
    return result

print(solution())
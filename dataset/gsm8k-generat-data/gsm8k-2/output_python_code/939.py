def solution():
    """Lloyd, Mark, and Michael have their Pokemon cards collection. Currently, Mark has thrice as many cards as Lloyd but has 10 fewer cards than Michael. If Michael has 100 cards now, how many more cards should they collect so that all three of them will have a total of 300 cards?"""
    michael_cards = 100
    mark_cards = michael_cards - 10
    lloyd_cards = mark_cards // 3
    total_cards = michael_cards + mark_cards + lloyd_cards
    cards_needed = 300 - total_cards
    result = cards_needed
    return result

print(solution())
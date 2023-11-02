def solution():
    """There are 120 cards in a box. If 2/5 of the cards are red, exactly 5/9 of the remainder are black, and the rest are green, calculate the number of green cards in the box?"""
    total_cards = 120
    red_cards = (2/5) * total_cards
    black_cards = (5/9) * (total_cards - red_cards)
    green_cards = total_cards - red_cards - black_cards
    result = green_cards
    return result

print(solution())
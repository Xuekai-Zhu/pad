def solution():
    total_cards = 120  # There are 120 cards in the box
    red_cards = (2/5) * total_cards  # 2/5 of the cards are red
    remaining_cards = total_cards - red_cards  # Calculate the number of cards that are not red
    black_cards = (5/9) * remaining_cards  # 5/9 of the remaining cards are black
    green_cards = remaining_cards - black_cards  # The remaining cards are green
    result = green_cards
    return result

print(solution())
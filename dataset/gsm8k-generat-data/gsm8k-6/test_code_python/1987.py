def solution():
    # Calculate the number of red cards
    red_cards = (2/5) * 120

    # Calculate the remainder of cards after taking out the red ones
    remaining_cards = 120 - red_cards

    # Calculate the number of black cards in the remainder
    black_cards = (5/9) * remaining_cards

    # Calculate the number of green cards in the box
    green_cards = remaining_cards - black_cards

    result = green_cards
    return result

print(solution())
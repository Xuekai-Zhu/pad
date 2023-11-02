def solution():
    """There are 120 cards in a box. If 2/5 of the cards are red, exactly 5/9 of the remainder are black, and the rest are green, calculate the number of green cards in the box?"""
    # Define the total number of cards in the box
    total_cards = 120

    # Calculate the number of red cards
    red_cards = total_cards * (2/5)

    # Calculate the number of non-red cards
    non_red_cards = total_cards - red_cards

    # Calculate the number of black cards
    black_cards = non_red_cards * (5/9)

    # Calculate the number of green cards
    green_cards = total_cards - red_cards - black_cards

    result = green_cards
    return result

print(solution())
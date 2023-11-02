def solution():
    """There are 120 cards in a box. If 2/5 of the cards are red, exactly 5/9 of the remainder are black, and the rest are green, calculate the number of green cards in the box?"""
    # Get the number of red cards
    red_cards = 2/5 * 120
    
    # Calculate the remainder of cards after removing the red ones
    remaining_cards = 120 - red_cards
    
    # Calculate the number of black cards in the remaining cards
    black_cards = 5/9 * remaining_cards
    
    # Calculate the number of green cards
    green_cards = remaining_cards - black_cards
    
    # Display the number of green cards
    result = green_cards
    return result

print(solution())
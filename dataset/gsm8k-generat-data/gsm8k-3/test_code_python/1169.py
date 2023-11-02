def solution():
    """Ben has four boxes with ten basketball cards in each box. His mother gave him five boxes with eight baseball cards. If he gives 58 cards to his classmates, how many cards does he have left?"""
    # Calculate the total number of cards Ben started with
    starting_cards = 4 * 10 + 5 * 8

    # Subtract the cards he gave to his classmates
    remaining_cards = starting_cards - 58

    # Display the number of cards Ben has left
    result = remaining_cards
    return result

print(solution())
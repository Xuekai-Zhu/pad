def solution():
    """Ben has four boxes with ten basketball cards in each box. His mother gave him five boxes with eight baseball cards. If he gives 58 cards to his classmates, how many cards does he have left?"""
    # Define the initial number of basketball cards and baseball cards
    basketball_cards = 4 * 10
    baseball_cards = 5 * 8

    # Calculate the total number of cards Ben has
    total_cards = basketball_cards + baseball_cards

    # Subtract the number of cards he gives to his classmates
    remaining_cards = total_cards - 58

    # return the result
    result = remaining_cards
    return result

print(solution())
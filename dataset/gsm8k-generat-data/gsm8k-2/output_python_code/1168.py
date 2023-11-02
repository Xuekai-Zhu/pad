def solution():
    """Ben has four boxes with ten basketball cards in each box. His mother gave him five boxes with eight baseball cards. If he gives 58 cards to his classmates, how many cards does he have left?"""
    basketball_cards = 4 * 10
    baseball_cards = 5 * 8
    total_cards = basketball_cards + baseball_cards - 58
    result = total_cards
    return result

print(solution())
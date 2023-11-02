def solution():
    basketball_cards = 4 * 10  # Ben has 4 boxes with 10 basketball cards each
    baseball_cards = 5 * 8  # Ben's mother gave him 5 boxes with 8 baseball cards each
    total_cards = basketball_cards + baseball_cards  # Total number of cards Ben has
    cards_given = 58  # Ben gives 58 cards to his classmates

    # Calculate the number of cards Ben has left
    cards_left = total_cards - cards_given
    result = cards_left
    return result

print(solution())
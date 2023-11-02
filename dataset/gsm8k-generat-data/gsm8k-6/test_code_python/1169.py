def solution():
    # Calculate the initial number of cards Ben has
    num_basketball_cards = 4 * 10
    num_baseball_cards = 5 * 8
    total_cards = num_basketball_cards + num_baseball_cards

    # Calculate the number of cards Ben has left after giving 58 to his classmates
    cards_left = total_cards - 58
    result = cards_left
    return result

print(solution())
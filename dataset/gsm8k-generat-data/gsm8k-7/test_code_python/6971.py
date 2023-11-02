def solution():
    num_hockey_cards = 200
    num_football_cards = 4 * num_hockey_cards
    num_baseball_cards = num_football_cards - 50

    # Calculate the total number of cards in the bag
    total_cards = num_hockey_cards + num_football_cards + num_baseball_cards
    result = total_cards
    return result

print(solution())
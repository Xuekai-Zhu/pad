def solution():
    hockey_cards = 200  # There are 200 hockey cards in the bag
    football_cards = 4 * hockey_cards  # There are 4 times as many football cards as hockey cards
    baseball_cards = football_cards - 50  # There are 50 fewer baseball cards than football cards

    # Calculate the total number of cards in the bag
    total_cards = hockey_cards + football_cards + baseball_cards
    result = total_cards
    return result

print(solution())
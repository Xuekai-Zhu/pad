def solution():
    # Find the number of football cards in the bag
    football_cards = 4 * 200

    # Find the number of baseball cards in the bag
    baseball_cards = football_cards - 50

    # Calculate the total number of cards in the bag
    total_cards = football_cards + baseball_cards + 200  # 200 hockey cards

    result = total_cards
    return result

print(solution())
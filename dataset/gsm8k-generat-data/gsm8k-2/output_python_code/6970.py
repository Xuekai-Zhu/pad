def solution():
    """A bag contains 50 fewer baseball cards than football cards. There are 4 times as many football cards as hockey cards. If there are 200 hockey cards in the bag, how many cards are there altogether?"""
    hockey_cards = 200
    football_cards = 4 * hockey_cards
    baseball_cards = football_cards - 50
    total_cards = hockey_cards + football_cards + baseball_cards
    result = total_cards
    return result

print(solution())
def solution():
    """A bag contains 50 fewer baseball cards than football cards. There are 4 times as many football cards as hockey cards. If there are 200 hockey cards in the bag, how many cards are there altogether?"""
    # Define the number of hockey cards
    hockey_cards = 200

    # Calculate the number of football cards
    football_cards = 4 * hockey_cards

    # Calculate the number of baseball cards
    baseball_cards = football_cards - 50

    # Calculate the total number of cards
    total_cards = hockey_cards + football_cards + baseball_cards

    # Display the total number of cards
    result = total_cards
    return result

print(solution())
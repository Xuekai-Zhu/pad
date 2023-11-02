def solution():
    """Jim had 365 trading cards. He gives 8 sets of cards to his brother, 5 sets of cards to his sister, and 2 sets of cards to his friend. How many cards did he give away, assuming 1 set has 13 trading cards?"""
    # Define the total number of trading cards
    total_cards = 365

    # Calculate the number of cards in one set
    cards_per_set = 13

    # Calculate the total number of sets given away
    total_sets = 8 + 5 + 2

    # Calculate the total number of cards given away
    total_cards_given_away = cards_per_set * total_sets

    # return the result
    result = total_cards_given_away
    return result

print(solution())
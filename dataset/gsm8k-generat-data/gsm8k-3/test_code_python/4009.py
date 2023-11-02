def solution():
    """Jim had 365 trading cards. He gives 8 sets of cards to his brother, 5 sets of cards to his sister, and 2 sets of cards to his friend. How many cards did he give away, assuming 1 set has 13 trading cards?"""
    # Define the number of cards in one set
    CARDS_PER_SET = 13

    # Define the number of sets given to each recipient
    brother_sets = 8
    sister_sets = 5
    friend_sets = 2

    # Calculate the total number of sets given away
    total_sets = brother_sets + sister_sets + friend_sets

    # Calculate the total number of cards given away
    total_cards = total_sets * CARDS_PER_SET

    # Display the total number of cards given away
    result = total_cards
    return result

print(solution())
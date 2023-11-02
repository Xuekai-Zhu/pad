def solution():
    """Marcus takes a deck of standard playing cards and takes out all the face cards and the 8's. Mark picks a card at random and then replaces it 36 times. How many times should he expect to pick a card that's both red and has a number divisible by 3?"""
    # Define the number of cards in the deck
    DECK_SIZE = 36

    # Define the number of red cards
    RED_CARDS = 18

    # Define the number of cards divisible by 3
    DIVISIBLE_BY_3 = 12

    # Define the probability of choosing a red card
    RED_PROBABILITY = 18 / 36

    # Define the probability of choosing a card divisible by 3
    DIVISIBLE_BY_3_PROBABILITY = 12 / 36

    # Calculate the probability of choosing a red card AND a card divisible by 3
    COMBINED_PROBABILITY = RED_PROBABILITY * DIVISIBLE_BY_3_PROBABILITY

    # Calculate the expected number of times of choosing a red card AND a card divisible by 3 in 36 picks
    expected_picks = COMBINED_PROBABILITY * 36

    # Display the expected number of picks
    result = expected_picks
    return result

print(solution())
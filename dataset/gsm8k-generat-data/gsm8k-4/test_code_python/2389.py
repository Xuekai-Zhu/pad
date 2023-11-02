def solution():
    """Marcus takes a deck of standard playing cards and takes out all the face cards and the 8's. Mark picks a card at random and then replaces it 36 times. How many times should he expect to pick a card that's both red and has a number divisible by 3?"""
    # Define the number of cards
    num_cards = 36

    # Define the number of red cards with a number divisible by 3
    num_red_div_3 = 2

    # Calculate the probability of picking a red card with a number divisible by 3
    probability = num_red_div_3 / 28

    # Calculate the expected number of times a card with the desired characteristics is picked
    expected_picks = num_cards * probability

    result = expected_picks
    return result

print(solution())
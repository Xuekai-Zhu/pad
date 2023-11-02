def solution():
    """The number of cards in a card game was 500. Two friends Ellis and Orion, playing together, divided the cards in the ratio of 11:9. How many more cards did Ellis get than Orion?"""
    # Define the total number of cards
    total_cards = 500

    # Calculate the number of cards Ellis and Orion each received
    ellis_cards = (11 / 20) * total_cards
    orion_cards = (9 / 20) * total_cards

    # Calculate the difference in the number of cards that Ellis and Orion received
    difference = ellis_cards - orion_cards

    # Display the difference in the number of cards that Ellis received
    result = difference
    return result

print(solution())
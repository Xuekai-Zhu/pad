def solution():
    """The number of cards in a card game was 500. Two friends Ellis and Orion, playing together, divided the cards in the ratio of 11:9. How many more cards did Ellis get than Orion?"""
    total_cards = 500
    ellis_cards = (11 / 20) * total_cards
    orion_cards = (9 / 20) * total_cards
    difference = ellis_cards - orion_cards
    result = difference
    return result

print(solution())
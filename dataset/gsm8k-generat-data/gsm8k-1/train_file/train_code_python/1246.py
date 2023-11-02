def solution():
    """The number of cards in a card game was 500. Two friends Ellis and Orion, playing together, divided the cards in the ratio of 11:9. How many more cards did Ellis get than Orion?"""
    total_cards = 500
    ellis_ratio = 11
    orion_ratio = 9
    total_ratio = ellis_ratio + orion_ratio
    ellis_share = (ellis_ratio / total_ratio) * total_cards
    orion_share = (orion_ratio / total_ratio) * total_cards
    difference = ellis_share - orion_share
    result = difference
    return result

print(solution())
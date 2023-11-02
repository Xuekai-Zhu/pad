def solution():
    total_cards = 500  # The total number of cards in the game
    ratio = 11/9  # The ratio in which the cards are divided

    # Calculate the number of cards Ellis and Orion each get
    ellis_cards = (11 / (11 + 9)) * total_cards
    orion_cards = (9 / (11 + 9)) * total_cards

    # Calculate the difference in the number of cards Ellis and Orion get
    difference = ellis_cards - orion_cards
    result = difference
    return result

print(solution())
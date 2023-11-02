def solution():
    # Find out how many cards the class would make if everyone made 8
    total_cards_made = 30 * 8  # number of kids x number of cards each kid makes

    # Find how many more cards are needed to reach 1000
    cards_needed = 1000 - total_cards_made
    result = cards_needed
    return result

print(solution())
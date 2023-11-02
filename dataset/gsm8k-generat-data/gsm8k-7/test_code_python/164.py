def solution():
    starting_cards = 30
    tuesday_cards = starting_cards / 2
    wednesday_cards = 12
    thursday_cards = tuesday_cards / 3
    total_cards = starting_cards - tuesday_cards + wednesday_cards + thursday_cards
    result = total_cards
    return result

print(solution())
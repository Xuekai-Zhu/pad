def solution():
    starting_cards = 16
    given_cards = starting_cards * (3/8)
    given_cards += 2
    remaining_cards = starting_cards - given_cards
    percentage_left = remaining_cards / starting_cards * 100
    result = round(percentage_left, 2)
    return result

print(solution())
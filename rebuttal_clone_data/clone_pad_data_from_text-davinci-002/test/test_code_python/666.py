def solution():
     basketball_cards = 4 * 10
     baseball_cards = 5 * 8
     total_cards = basketball_cards + baseball_cards
     cards_given_away = 58
     cards_left = total_cards - cards_given_away
     result = cards_left
     return result

print(solution())
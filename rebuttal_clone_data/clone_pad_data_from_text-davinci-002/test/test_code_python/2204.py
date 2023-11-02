def solution():
     initial_cards = 16
     cards_given_away = (3/8) * initial_cards + 2
     cards_left = initial_cards - cards_given_away
     percent_left = (cards_left/initial_cards) * 100
     result = percent_left
     return result

print(solution())
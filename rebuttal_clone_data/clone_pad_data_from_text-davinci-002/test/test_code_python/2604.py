def solution():
     cards_per_box = 10
     boxes_given_away = 2
     boxes_remaining = 5
     total_cards = (cards_per_box * boxes_given_away) + (cards_per_box * boxes_remaining) + 5
     result = total_cards
     return result

print(solution())
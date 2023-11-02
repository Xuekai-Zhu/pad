def solution():
     cards_per_week = 6
     weeks_to_give = 2
     cards_given = 2
     starting_cards = 20
     total_cards = 40
     weeks = (total_cards - starting_cards) / (cards_per_week - cards_given)
     result = weeks
     return result

print(solution())
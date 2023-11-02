def solution():
     total_cards = 130
     cards_kept = 15
     cards_given_to_miguel = total_cards - cards_kept
     cards_given_to_friends = 8 * 12
     cards_given_to_sisters = (total_cards - cards_kept - cards_given_to_miguel - cards_given_to_friends) / 2
     result = cards_given_to_sisters
     return result

print(solution())
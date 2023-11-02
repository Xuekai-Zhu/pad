def solution():
     rare_cards = 19
     uncommon_cards = 11
     common_cards = 30
     rare_card_cost = 1
     uncommon_card_cost = 0.5
     common_card_cost = 0.25
     rare_total_cost = rare_cards * rare_card_cost
     uncommon_total_cost = uncommon_cards * uncommon_card_cost
     common_total_cost = common_cards * common_card_cost
     total_deck_cost = rare_total_cost + uncommon_total_cost + common_total_cost
     result = total_deck_cost
     
     return result

print(solution())
def solution():
     num_cards = 2000
     value_per_card = 0.05
     cost_per_comic = 6
     total_value = num_cards * value_per_card
     num_comics = total_value // cost_per_comic
     money_leftover = total_value - (num_comics * cost_per_comic)
     result = money_leftover
     return result

print(solution())
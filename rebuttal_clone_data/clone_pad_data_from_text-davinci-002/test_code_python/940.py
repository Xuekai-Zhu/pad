def solution():
     total_cards = 300
     michael_cards = 100
     mark_cards = michael_cards - 10
     lloyd_cards = mark_cards / 3
     cards_to_collect = total_cards - (michael_cards + mark_cards + lloyd_cards)
     result = cards_to_collect
     return result

print(solution())
def solution():
     total_cards = 500
     ellis_cards = total_cards * (11/20)
     orion_cards = total_cards * (9/20)
     ellis_more_cards = ellis_cards - orion_cards
     result = ellis_more_cards
     return result

print(solution())
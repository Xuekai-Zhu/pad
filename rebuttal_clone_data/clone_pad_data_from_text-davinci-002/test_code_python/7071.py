def solution():
     cards_left = 46
     cards_eaten = (8 - cards_left) / 2
     cards_started = cards_left + cards_eaten
     result = cards_started
     return result

print(solution())
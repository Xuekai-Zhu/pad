def solution():
     baseball_cards = 25
     baseball_bat = 10
     baseball_glove = 30
     baseball_cleats = 10
     total_money = baseball_cards + baseball_bat + (baseball_glove * 0.8) + (baseball_cleats * 2)
     result = total_money
     return result

print(solution())
def solution():
     candy_necklaces = 8
     packs_opened = 9
     candy_left = 40
     candy_given_away = candy_necklaces * packs_opened - candy_left
     result = candy_given_away / candy_necklaces
     return result

print(solution())
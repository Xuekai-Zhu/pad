def solution():
     chickens = 46
     eggs_per_chicken_per_week = 6
     # 8 weeks * (46 chickens * 6 eggs per week) = 2,208 eggs
     eggs = 8 * (chickens * eggs_per_chicken_per_week)
     # 2,208 eggs / 12 eggs per dozen = 184 dozen
     dozens_of_eggs = eggs / 12
     # 184 dozen * $3 per dozen of eggs = $552
    total_money = dozens_of_eggs * 3
     return total_money

print(solution())
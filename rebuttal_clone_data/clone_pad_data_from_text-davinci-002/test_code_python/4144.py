def solution():
     money_total = 32
     bread_cost = 3
     candy_cost = 2
     turkey_cost = (money_total - bread_cost - candy_cost) / 3
     money_left = money_total - (bread_cost + candy_cost + turkey_cost)
     result = money_left
     
     return result

print(solution())
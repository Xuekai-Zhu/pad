def solution():
     cost_per_dozen_apples = 14
     cost_per_kiwi = 10
     cost_per_banana = cost_per_kiwi / 2
     remaining_money = 50 - (cost_per_kiwi + cost_per_banana) - (2 * 3.50)
     max_apples = remaining_money / cost_per_dozen_apples
     result = max_apples
     return result

print(solution())
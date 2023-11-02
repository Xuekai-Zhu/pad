def solution():
     chicken_cost = 16 / 2
     beef_cost = 16 - chicken_cost
     result = chicken_cost + (beef_cost / 3)
     return result

print(solution())
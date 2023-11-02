def solution():
     apples = 2
     pears = apples + 2
     bananas = pears + 3
     total_fruit = apples + pears + bananas
     if total_fruit == 19:
         result = bananas
         return result

print(solution())
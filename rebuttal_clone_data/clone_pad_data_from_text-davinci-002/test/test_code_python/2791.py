def solution():
     apples = 7
     oranges = 8
     mangoes = 15
     apples_taken = 2
     oranges_taken = 2 * apples_taken
     mangoes_taken = (2/3) * mangoes
     total_fruit_taken = apples_taken + oranges_taken + mangoes_taken
     remaining_fruit = apples + oranges + mangoes - total_fruit_taken
     result = remaining_fruit
     return result

print(solution())
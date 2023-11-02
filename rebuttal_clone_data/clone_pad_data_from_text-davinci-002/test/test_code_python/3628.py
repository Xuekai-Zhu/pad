def solution():
     bottles_bought = 24
     bottles_drank_1 = bottles_bought / 3
     bottles_left_1 = bottles_bought - bottles_drank_1
     bottles_drank_2 = bottles_left_1 / 2
     bottles_left_2 = bottles_left_1 - bottles_drank_2
     result = bottles_left_2
     return result

print(solution())
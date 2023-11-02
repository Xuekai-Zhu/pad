def solution():
     initial_soda = 3
     drank_soda = 0.9
     given_soda = 0.7
     given_soda_two = 0.7
     left_soda = initial_soda - (drank_soda + given_soda + given_soda_two)
     result = left_soda * 100
     return result

print(solution())
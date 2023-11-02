def solution():
   bottles_in_refrigerator = 4
   bottles_in_pantry = 4
   bottles_bought = 5
   bottles_drank = 3
   total_bottles = bottles_in_refrigerator + bottles_in_pantry + bottles_bought - bottles_drank
   result = total_bottles
   return result

print(solution())
def solution():
     poisonous_mushrooms = 32 - 9
     safe_mushrooms = 9
     uncertain_mushrooms = poisonous_mushrooms - (2 * safe_mushrooms)
     result = uncertain_mushrooms
     return result

print(solution())
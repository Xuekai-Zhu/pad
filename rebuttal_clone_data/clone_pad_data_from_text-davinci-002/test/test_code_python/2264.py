def solution():
     goats = 3
     llamas = goats * 2
     cost_of_goats = goats * 400
     cost_of_llamas = llamas * (400 * 1.5)
     total_cost = cost_of_goats + cost_of_llamas
     result = total_cost
     return result

print(solution())
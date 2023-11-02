def solution():
     initial_cost = 150
     per_mile_cost = 0.50
     total_miles = 620 + 744
     total_cost = initial_cost + (total_miles * per_mile_cost)
     result = total_cost
     return result

print(solution())
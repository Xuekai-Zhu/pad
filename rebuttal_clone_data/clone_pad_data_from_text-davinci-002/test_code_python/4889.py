def solution():
     total_birds = 15
     fraction_ducks = 1/3
     ducks = total_birds * fraction_ducks
     chickens = total_birds - ducks
     cost_per_chicken = 2
     total_cost = chickens * cost_per_chicken
     return total_cost

print(solution())
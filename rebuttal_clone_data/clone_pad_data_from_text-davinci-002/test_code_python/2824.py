def solution():
     pounds_of_beef = 100
     pounds_per_taco = 0.25
     tacos_made = pounds_of_beef / pounds_per_taco
     cost_per_taco = 1.5
     revenue_per_taco = 2
     total_profit = tacos_made * (revenue_per_taco - cost_per_taco)
     result = total_profit
     return result

print(solution())
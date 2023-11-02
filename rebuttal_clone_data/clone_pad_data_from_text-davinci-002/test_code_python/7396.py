def solution():
     ml_per_bottle = 750
     servings_per_bottle = 16
     cost_per_bottle = 30.00
     cost_per_serving = 8.00
     profit = cost_per_bottle - (servings_per_bottle * cost_per_serving)
     result = profit
     return result

print(solution())
def solution():
     monthly_cost = 12
     texts = 60
     minutes = 60
     cost_per_text = 1
     cost_per_minute = 3
     cost_of_texts = texts * cost_per_text
     cost_of_calls = minutes * cost_per_minute
     total_cost = cost_of_texts + cost_of_calls
     result = monthly_cost - total_cost
     return result

print(solution())
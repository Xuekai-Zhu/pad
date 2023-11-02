def solution():
    
    total_budget = 3000
    food_budget = total_budget / 3
    supplies_budget = total_budget / 4
    wages_budget = total_budget - food_budget - supplies_budget
    result = wages_budget
    return result

print(solution())
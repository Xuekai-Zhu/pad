def solution():
    """Abe owns a restaurant. Every month he spends a third of his budget on food, a quarter of his budget on restaurant supplies, and the rest of his budget on employee wages. If his budget is $3000 and he uses it up every month, how much is he spending on wages?"""
    total_budget = 3000
    food_budget = total_budget / 3
    supplies_budget = total_budget / 4
    wages_budget = total_budget - food_budget - supplies_budget
    result = wages_budget
    return result

print(solution())
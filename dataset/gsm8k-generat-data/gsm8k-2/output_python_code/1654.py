def solution():
    """Abe owns a restaurant. Every month he spends a third of his budget on food, a quarter of his budget on restaurant supplies, and the rest of his budget on employee wages. If his budget is $3000 and he uses it up every month, how much is he spending on wages?"""
    budget = 3000
    food_cost = budget / 3
    supplies_cost = budget / 4
    wage_cost = budget - food_cost - supplies_cost
    result = wage_cost
    return result

print(solution())
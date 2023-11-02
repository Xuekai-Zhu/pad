def solution():
    
    total_budget = 1000
    food_budget = 0.3 * total_budget
    accommodation_budget = 0.15 * total_budget
    entertainment_budget = 0.25 * total_budget
    coursework_budget = total_budget - food_budget - accommodation_budget - entertainment_budget
    result = coursework_budget
    return result

print(solution())
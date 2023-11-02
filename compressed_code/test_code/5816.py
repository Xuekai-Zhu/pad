def solution():
    
    budget = 1000
    food_spending = budget * 0.3
    accommodation_spending = budget * 0.15
    entertainment_spending = budget * 0.25
    coursework_spending = budget - food_spending - accommodation_spending - entertainment_spending
    result = coursework_spending
    return result

print(solution())
def solution():
    budget_per_semester = 1000 # James has a budget of $1000 per semester
    food_expenses = 0.3 * budget_per_semester # James spends 30% of his budget on food
    accommodation_expenses = 0.15 * budget_per_semester # James spends 15% of his budget on accommodation
    entertainment_expenses = 0.25 * budget_per_semester # James spends 25% of his budget on entertainment
    coursework_materials_expenses = budget_per_semester - food_expenses - accommodation_expenses - entertainment_expenses # James spends the rest on coursework materials
    result = coursework_materials_expenses
    return result

print(solution())
def solution():
    """James is a first-year student at a University in Chicago. He has a budget of $1000 per semester. He spends 30% of his money on food, 15% on accommodation, 25% on entertainment, and the rest on coursework materials. How much money does he spend on coursework materials?"""
    total_budget = 1000
    food_budget = 0.3 * total_budget
    accommodation_budget = 0.15 * total_budget
    entertainment_budget = 0.25 * total_budget
    coursework_budget = total_budget - food_budget - accommodation_budget - entertainment_budget
    result = coursework_budget
    return result

print(solution())
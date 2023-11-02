def solution():
    """James is a first-year student at a University in Chicago. He has a budget of $1000 per semester. He spends 30% of his money on food, 15% on accommodation, 25% on entertainment, and the rest on coursework materials. How much money does he spend on coursework materials?"""
    budget = 1000
    food_spending = budget * 0.3
    accommodation_spending = budget * 0.15
    entertainment_spending = budget * 0.25
    coursework_spending = budget - food_spending - accommodation_spending - entertainment_spending
    result = coursework_spending
    return result

print(solution())
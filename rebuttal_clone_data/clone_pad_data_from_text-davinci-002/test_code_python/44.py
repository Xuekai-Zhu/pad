def solution():
     """James is a first-year student at a University in Chicago. He has a budget of $1000 per semester. He spends 30% of his money on food, 15% on accommodation, 25% on entertainment, and the rest on coursework materials. How much money does he spend on coursework materials?"""
     semester_budget = 1000
     food_percent = 30
     food_cost = semester_budget * (food_percent / 100)
     accommodation_percent = 15
     accommodation_cost = semester_budget * (accommodation_percent / 100)
     entertainment_percent = 25
     entertainment_cost = semester_budget * (entertainment_percent / 100)
     coursework_cost = semester_budget - food_cost - accommodation_cost - entertainment_cost
     result = coursework_cost
     return result

print(solution())
def solution():
     
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
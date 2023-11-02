def solution():
    
    grandparents_money = 4 * 50
    bird_cost = 20
    total_birds = grandparents_money // bird_cost
    total_wings = total_birds * 2
    result = total_wings
    return result

print(solution())
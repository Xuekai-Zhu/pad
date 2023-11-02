def solution():
    
    money_from_grandparents = 50 * 4
    cost_per_bird = 20
    total_birds = money_from_grandparents // cost_per_bird
    total_wings = total_birds * 2
    result = total_wings
    return result

print(solution())
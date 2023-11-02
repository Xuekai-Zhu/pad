def solution():
    goats = 360 * (5/12)
    sheep = 360 * (7/12)
    total_animals = goats + sheep
    total_goats = total_animals * (5/12)
    total_sheep = total_animals * (7/12)
    cost_of_goats = total_goats * 40
    cost_of_sheep = total_sheep * 30
    total_cost = cost_of_goats + cost_of_sheep
    result = total_cost
    
    return result

print(solution())
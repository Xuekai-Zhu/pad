def solution():
    
    cans_per_carton = 20
    total_cartons = 50
    loaded_cartons = 40
    cans_left = (total_cartons - loaded_cartons) * cans_per_carton
    result = cans_left
    return result

print(solution())
def solution():
    
    cans_per_carton = 20
    total_cartons = 50
    loaded_cartons = 40
    remaining_cartons = total_cartons - loaded_cartons
    remaining_cans = remaining_cartons * cans_per_carton
    result = remaining_cans
    return result

print(solution())
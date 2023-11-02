def solution():
    
    initial_land = 300
    land_cost = 20
    land1_cost = 8000
    land2_cost = 4000
    land1_size = land1_cost / land_cost
    land2_size = land2_cost / land_cost
    total_land = initial_land + land1_size + land2_size
    result = total_land
    return result

print(solution())
def solution():
    
    land_cost = 20
    initial_land = 300
    bought_land_cost = 8000 + 4000
    bought_land_size = bought_land_cost / land_cost
    total_land_size = initial_land + bought_land_size
    result = total_land_size
    return result

print(solution())
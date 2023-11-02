def solution():
    johnson_yield = 80 #corn every two months from 1 hectare
    johnson_field = 1 #hectare
    neighbor_field = 2 #hectares
    neighbor_yield = johnson_yield * 2 #twice the yield of Johnson
    total_months = 6
    total_harvested = (johnson_yield * johnson_field * (total_months//2)) + (neighbor_yield * neighbor_field * (total_months//2))
    result = total_harvested
    return result

print(solution())
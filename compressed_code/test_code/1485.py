def solution():
    
    johnson_yield = 80
    neighbor_yield = 2 * johnson_yield * 2  
    total_yield = (johnson_yield * 3) + (neighbor_yield * 3)  
    result = total_yield
    return result

print(solution())
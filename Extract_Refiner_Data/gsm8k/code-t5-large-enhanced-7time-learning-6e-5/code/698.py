def solution():
    
    gissela_gravel = 4000
    gordy_gravel = gissela_gravel + 800
    total_gravel = 11600
    gravel_per_truck = total_gravel - gissela_gravel - gordy_gravel
    result = gravel_per_truck
    return result

print(solution())
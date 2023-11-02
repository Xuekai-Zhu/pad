def solution():
    
    
    
    grady_red_cubes = 20
    grady_blue_cubes = 15
    
    
    gage_red_cubes = 10
    gage_blue_cubes = 12
    
    
    gage_red_cubes_received = (2/5) * grady_red_cubes
    
    
    gage_blue_cubes_received = (1/3) * grady_blue_cubes
    
    
    total_cubes = gage_red_cubes + gage_red_cubes_received + gage_blue_cubes + gage_blue_cubes_received
    
    result = total_cubes
    
    return result

print(solution())
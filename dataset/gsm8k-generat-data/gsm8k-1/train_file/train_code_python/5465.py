def solution():
    """Grady has 20 red numbered cubes and 15 blue numbered cubes. 
    He gives his friend Gage 2/5 of his red numbered cubes and 1/3 of the blue numbered cubes. 
    If Gage had 10 red numbered cubes and 12 blue numbered cubes, find the total number of cubes Gage has?"""
    
    # Grady's initial number of cubes
    grady_red_cubes = 20
    grady_blue_cubes = 15
    
    # Gage's cubes after receiving some from Grady
    gage_red_cubes = 10
    gage_blue_cubes = 12
    
    # 2/5 of Grady's red cubes is equal to Gage's red cubes
    gage_red_cubes_received = (2/5) * grady_red_cubes
    
    # 1/3 of Grady's blue cubes is equal to Gage's blue cubes
    gage_blue_cubes_received = (1/3) * grady_blue_cubes
    
    # Total number of cubes Gage has
    total_cubes = gage_red_cubes + gage_red_cubes_received + gage_blue_cubes + gage_blue_cubes_received
    
    result = total_cubes
    
    return result

print(solution())
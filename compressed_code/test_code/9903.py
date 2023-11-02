def solution():
    
    hermit_crabs = 45
    spiral_shells_per_crab = 3
    starfish_per_shell = 2
    
    
    total_shells = hermit_crabs * spiral_shells_per_crab
    
    
    total_starfish = total_shells * starfish_per_shell
    
    
    total_souvenirs = hermit_crabs + total_shells + total_starfish
    
    result = total_souvenirs
    return result

print(solution())
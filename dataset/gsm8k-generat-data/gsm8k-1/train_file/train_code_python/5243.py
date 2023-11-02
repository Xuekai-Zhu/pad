def solution():
    """Jackson collects 45 hermit crabs, 3 spiral shells per hermit crab, and 2 starfish per spiral shell. How many souvenirs does he collect total?"""
    hermit_crabs = 45
    spiral_shells_per_crab = 3
    starfish_per_shell = 2
    
    # Calculate total number of spiral shells
    total_shells = hermit_crabs * spiral_shells_per_crab
    
    # Calculate total number of starfish
    total_starfish = total_shells * starfish_per_shell
    
    # Calculate total number of souvenirs
    total_souvenirs = hermit_crabs + total_shells + total_starfish
    
    result = total_souvenirs
    return result

print(solution())
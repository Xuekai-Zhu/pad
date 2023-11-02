def solution():
    """Gilbert grows herbs in his yard to use in his cooking. At the beginning of the spring, he planted three basil bushes, a parsley plant, and two kinds of mint. Halfway through spring, one of the basil plants dropped seeds from a flower and made an extra basil plant grow. However, a rabbit came by the garden near the end of spring and ate all the mint. How many herb plants did Gilbert have when spring ended?"""
    basil_bushes = 3
    parsley_plant = 1
    mint_plants = 2
    
    # One extra basil plant grew
    basil_bushes += 1
    
    # The rabbit ate both mint plants
    mint_plants = 0
    
    total_plants = basil_bushes + parsley_plant + mint_plants
    
    result = total_plants
    
    return result

print(solution())
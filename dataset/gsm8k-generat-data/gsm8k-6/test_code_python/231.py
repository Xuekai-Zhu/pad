def solution():
    # Calculate the number of drops used to test each beaker
    drops_per_beaker = 3  
    
    # Calculate the total number of drops used to test all beakers
    total_drops = 45  
    
    # Calculate the number of beakers with copper ions
    beakers_with_copper = 8  
    
    # Calculate the number of beakers tested by dividing the total number of drops by the drops used per beaker
    total_beakers_tested = total_drops // drops_per_beaker  
    
    # Calculate the number of beakers without copper ions tested by subtracting the number of beakers with copper ions from the total beakers tested
    beakers_without_copper_tested = total_beakers_tested - beakers_with_copper  
    
    result = beakers_without_copper_tested
    return result

print(solution())
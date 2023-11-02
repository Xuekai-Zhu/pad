def solution():
    
    utensils_per_pack = 30
    spoons_per_pack = utensils_per_pack / 3  
    spoons_needed = 50
    packs_needed = spoons_needed / spoons_per_pack

    result = packs_needed
    return result

print(solution())
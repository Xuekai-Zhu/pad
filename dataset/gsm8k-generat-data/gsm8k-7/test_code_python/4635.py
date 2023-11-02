def solution():
    packs = 15
    red_per_pack = 1   # initially each pack has one red pencil inside
    extra_red_packs = 3
    extra_red_per_pack = 2
    
    # Calculate the total number of red pencils in all packs
    total_red_pencils = packs * red_per_pack
    
    # Add the extra red pencils from the packs that have two extra
    total_red_pencils += extra_red_packs * extra_red_per_pack
    
    result = total_red_pencils
    return result

print(solution())
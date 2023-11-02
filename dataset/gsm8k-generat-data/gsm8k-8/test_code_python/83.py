def solution():
    Paityn_red_hats = 20
    Paityn_blue_hats = 24
    
    # Calculate Zola's hats
    Zola_red_hats = 4/5 * Paityn_red_hats
    Zola_blue_hats = 2 * Paityn_blue_hats
    
    # Calculate the total number of hats
    total_hats = Paityn_red_hats + Paityn_blue_hats + Zola_red_hats + Zola_blue_hats
    
    # Calculate the hats each person gets
    hats_each = total_hats // 2
    
    result = hats_each
    return result

print(solution())
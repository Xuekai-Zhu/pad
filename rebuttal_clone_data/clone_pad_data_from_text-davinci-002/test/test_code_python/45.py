def solution():
    
    paityn_red_hats = 20
    paityn_blue_hats = 24
    zola_red_hats = (4 / 5) * paityn_red_hats
    zola_blue_hats = 2 * paityn_blue_hats
    total_hats = paityn_red_hats + paityn_blue_hats + zola_red_hats + zola_blue_hats
    hats_per_person = total_hats / 2
    result = hats_per_person
    return result

print(solution())
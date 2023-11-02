def solution():
    paityn_red_hats = 20  # Paityn has 20 red hats
    paityn_blue_hats = 24  # Paityn has 24 blue hats
    zola_red_hats = (4/5) * paityn_red_hats  # Zola has 4/5 times as many red hats as Paityn
    zola_blue_hats = 2 * paityn_blue_hats   # Zola has twice as many blue hats as Paityn

    total_hats = paityn_red_hats + paityn_blue_hats + zola_red_hats + zola_blue_hats  # Total number of hats
    hats_each = total_hats / 2   # Divide the hats equally between Paityn and Zola

    result = hats_each
    return result

print(solution())
def solution():
    paityn_red_hats = 20
    paityn_blue_hats = 24
    zola_red_hats = (4/5) * paityn_red_hats
    zola_blue_hats = 2 * paityn_blue_hats

    total_red_hats = paityn_red_hats + zola_red_hats
    total_blue_hats = paityn_blue_hats + zola_blue_hats

    total_hats = total_red_hats + total_blue_hats

    paityn_share = total_hats / 2
    zola_share = total_hats / 2

    result = (paityn_share, zola_share)
    return result

print(solution())
def solution():
    """Paityn has 20 red hats and 24 blue hats. Her friend Zola has 4/5 times as many red hats as she has and twice the number of blue hats. If they combine all the hats together and share them equally between themselves, calculate the number of hats each gets."""
    paityn_red = 20
    paityn_blue = 24
    zola_red = int((4/5) * paityn_red)
    zola_blue = 2 * paityn_blue
    total_red = paityn_red + zola_red
    total_blue = paityn_blue + zola_blue
    total_hats = total_red + total_blue
    paityn_share = total_hats / 2
    zola_share = total_hats / 2
    result = (paityn_share, zola_share)
    return result

print(solution())
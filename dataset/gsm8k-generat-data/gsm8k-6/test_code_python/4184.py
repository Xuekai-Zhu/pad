def solution():
    total_gnomes = 28
    red_hats = (3/4) * total_gnomes
    blue_hats = total_gnomes - red_hats
    big_noses = 0.5 * total_gnomes
    small_noses = total_gnomes - big_noses
    big_blue_hats = 6
    small_red_hats = small_noses - big_blue_hats
    small_red_hats = int(small_red_hats)  # round down to whole number
    result = small_red_hats
    return result

print(solution())
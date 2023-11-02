def solution():
    kendra_packs = 4  # Kendra has 4 packs of pens
    tony_packs = 2  # Tony has 2 packs of pens
    pens_per_pack = 3  # There are 3 pens in each pack
    pens_to_keep = 2  # Kendra and Tony each keep 2 pens

    # Calculate the total number of pens
    kendra_pens = kendra_packs * pens_per_pack
    tony_pens = tony_packs * pens_per_pack
    total_pens = kendra_pens + tony_pens

    # Subtract the pens kept by Kendra and Tony
    remaining_pens = total_pens - (pens_to_keep * 2)

    # Calculate the number of friends who can receive a pen
    friends = remaining_pens // 1
    result = friends
    return result

print(solution())
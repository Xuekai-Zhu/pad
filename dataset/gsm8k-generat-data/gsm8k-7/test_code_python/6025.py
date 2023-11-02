def solution():
    kendra_packs = 4
    tony_packs = 2
    pens_per_pack = 3
    pens_kept = 2

    # Calculate the total number of pens Kendra and Tony have
    total_pens = (kendra_packs + tony_packs) * pens_per_pack

    # Subtract the number of pens kept by Kendra and Tony
    total_pens -= pens_kept * 2

    # Calculate the number of friends that will receive pens
    num_friends = total_pens

    result = num_friends
    return result

print(solution())
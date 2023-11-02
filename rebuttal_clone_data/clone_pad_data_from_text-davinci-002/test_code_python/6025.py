def solution():
    kendra_packs = 4
    tony_packs = 2
    pens_per_pack = 3
    pens_needed = 2
    number_of_friends = (kendra_packs * pens_per_pack + tony_packs * pens_per_pack - pens_needed) / pens_needed
    result = number_of_friends
    return result

print(solution())
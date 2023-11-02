def solution():
    """Kendra has 4 packs of pens. Tony has 2 packs of pens. There are 3 pens in each pack. If Kendra and Tony decide to keep two pens each and give the remaining pens to their friends one pen per friend, how many friends will they give pens to?"""
    kendra_packs = 4
    tony_packs = 2
    pens_per_pack = 3
    total_pens = (kendra_packs + tony_packs) * pens_per_pack
    pens_kept = 4
    remaining_pens = total_pens - pens_kept
    friends = remaining_pens // 1
    result = friends
    return result

print(solution())
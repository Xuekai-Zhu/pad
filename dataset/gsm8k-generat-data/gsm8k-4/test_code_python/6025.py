def solution():
    """Kendra has 4 packs of pens. Tony has 2 packs of pens. There are 3 pens in each pack. If Kendra and Tony decide to keep two pens each and give the remaining pens to their friends one pen per friend, how many friends will they give pens to?"""
    # Define the number of packs of pens each person has
    kendra_packs = 4
    tony_packs = 2

    # Define the number of pens per pack
    pens_per_pack = 3

    # Calculate the total number of pens available
    total_pens = (kendra_packs + tony_packs) * pens_per_pack

    # Calculate the number of pens kept by Kendra and Tony
    pens_kept = 4

    # Calculate the number of pens available to give to friends
    pens_to_give = total_pens - pens_kept

    # Calculate the number of friends to give pens to
    friends = pens_to_give // 1

    # Return the result
    result = friends
    return result

print(solution())
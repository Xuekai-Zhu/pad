def solution():
    """Kendra has 4 packs of pens. Tony has 2 packs of pens. There are 3 pens in each pack. If Kendra and Tony decide to keep two pens each and give the remaining pens to their friends one pen per friend, how many friends will they give pens to?"""
    # Define the number of packs of pens each person has
    kendra_packs = 4
    tony_packs = 2

    # Define the number of pens in each pack
    pens_per_pack = 3

    # Calculate the total number of pens Kendra and Tony have
    total_pens = (kendra_packs + tony_packs) * pens_per_pack

    # Calculate the number of pens they keep for themselves
    keep_pens = 4

    # Calculate the number of pens they give away
    give_pens = total_pens - keep_pens

    # Calculate the number of friends they can give pens to
    num_friends = give_pens

    # Display the number of friends they can give pens to
    result = num_friends
    return result

print(solution())
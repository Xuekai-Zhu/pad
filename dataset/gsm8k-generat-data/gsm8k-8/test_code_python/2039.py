def solution():
    # Define variables
    total_marbles = 400
    marbles_per_pack = 10

    # Calculate the number of packs
    total_packs = total_marbles / marbles_per_pack

    # Calculate the number of packs given to Manny and Neil
    manny_packs = 1/4 * total_packs
    neil_packs = 1/8 * total_packs

    # Calculate the number of packs kept by Leo
    packs_kept = total_packs - manny_packs - neil_packs

    result = packs_kept
    return result

print(solution())
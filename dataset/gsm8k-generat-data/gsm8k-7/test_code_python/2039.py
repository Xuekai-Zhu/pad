def solution():
    total_marbles = 400
    marble_per_pack = 10
    num_packs = total_marbles / marble_per_pack

    manny_packs = num_packs * 0.25
    neil_packs = num_packs * 0.125

    packs_given = manny_packs + neil_packs
    packs_kept = num_packs - packs_given

    result = packs_kept
    return result

print(solution())
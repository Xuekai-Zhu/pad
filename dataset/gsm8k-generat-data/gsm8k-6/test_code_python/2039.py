def solution():
    # Find the total number of packs of marbles
    total_packs = 400 // 10

    # Find the number of packs of marbles given to Manny and Neil
    manny_packs = total_packs * 1/4
    neil_packs = total_packs * 1/8

    # Find the total number of packs of marbles given away
    given_away_packs = manny_packs + neil_packs

    # Find the number of packs of marbles that Leo kept
    kept_packs = total_packs - given_away_packs
    result = kept_packs
    return result

print(solution())
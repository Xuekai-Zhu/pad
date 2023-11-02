def solution():
    # Information about Jack Sparrow
    is_jack_sparrow_captain = True
    sings_at_sea = True
    # Check if Jack Sparrow knows any sea shantys
    if is_jack_sparrow_captain and sings_at_sea:
        knows_sea_shantys = True
    else:
        knows_sea_shantys = False
    return knows_sea_shantys

print(solution())
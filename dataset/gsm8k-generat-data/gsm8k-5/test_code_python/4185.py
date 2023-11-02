def solution():
    packs_bought = 9  # Emily bought 9 packs of candy necklaces
    necklaces_per_pack = 8  # Each pack had 8 candy necklaces
    necklaces_left = 40  # There were 40 candy necklaces left after her classmates took some

    # Calculate the total number of candy necklaces available
    total_necklaces = packs_bought * necklaces_per_pack

    # Calculate the number of necklaces Emily's classmates took
    necklaces_taken = total_necklaces - necklaces_left

    # Calculate the number of packs Emily opened for her classmates
    packs_opened = necklaces_taken // necklaces_per_pack
    result = packs_opened
    return result

print(solution())
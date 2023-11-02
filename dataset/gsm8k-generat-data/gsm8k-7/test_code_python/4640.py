def solution():
    colored_pencils = 14
    black_pencils = 35
    siblings = 3
    pencils_for_teresa = 10

    # Calculate the total number of pencils Teresa has
    total_pencils = colored_pencils + black_pencils

    # Subtract the number of pencils Teresa keeps for herself
    pencils_for_sharing = total_pencils - pencils_for_teresa

    # Divide the remaining pencils equally among the siblings
    pencils_per_sibling = pencils_for_sharing // siblings
    result = pencils_per_sibling
    return result

print(solution())
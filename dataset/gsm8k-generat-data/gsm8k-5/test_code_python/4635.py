def solution():
    packs_of_colored_pencils = 15
    red_pencils_per_pack = 1
    extra_red_pencils_per_pack = 2
    packs_with_extra_red_pencils = 3

    # Calculate the total number of red pencils
    total_red_pencils = (packs_of_colored_pencils * red_pencils_per_pack) + \
                        (extra_red_pencils_per_pack * packs_with_extra_red_pencils)

    result = total_red_pencils
    return result

print(solution())
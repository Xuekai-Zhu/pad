def solution():
    # Calculate the total number of red pencils without the extra ones
    red_pencils_per_pack = 1
    total_red_pencils = red_pencils_per_pack * 15

    # Calculate the total number of extra red pencils
    extra_red_pencils = 2 * 3

    # Calculate the total number of red pencils with the extra ones
    total_red_pencils_with_extra = total_red_pencils + extra_red_pencils
    result = total_red_pencils_with_extra
    return result

print(solution())
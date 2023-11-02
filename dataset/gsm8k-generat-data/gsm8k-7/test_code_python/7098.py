def solution():
    gertrude_fleas = 10
    maud_fleas = 5 * gertrude_fleas
    olive_fleas = gertrude_fleas / 2

    # Sum up the number of fleas for all the chickens
    total_fleas = gertrude_fleas + maud_fleas + olive_fleas
    result = total_fleas
    return result

print(solution())
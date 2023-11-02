def solution():
    # Calculate the total number of fleas
    olive_fleas = 10 / 2  # Olive has half the amount of fleas as Gertrude
    maud_fleas = 5 * olive_fleas  # Maud has 5 times the amount of fleas as Olive
    total_fleas = olive_fleas + maud_fleas + 10  # 10 fleas for Gertrude

    result = total_fleas
    return result

print(solution())
def solution():
    charlie_flutes = 1
    charlie_horns = 2
    charlie_harps = 1
    carli_flutes = charlie_flutes * 2
    carli_horns = charlie_horns / 2
    carli_harps = 0

    # Calculate the total number of instruments owned by Charlie and Carli
    total_instruments = charlie_flutes + charlie_horns + charlie_harps + carli_flutes + carli_horns + carli_harps
    result = total_instruments
    return result

print(solution())
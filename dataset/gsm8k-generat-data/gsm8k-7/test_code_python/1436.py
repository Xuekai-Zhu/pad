def solution():
    charlie_flutes = 1
    charlie_horns = 2
    charlie_harps = 1

    carli_flutes = charlie_flutes * 2
    carli_horns = charlie_horns / 2
    carli_harps = 0

    total_flutes = charlie_flutes + carli_flutes
    total_horns = charlie_horns + carli_horns
    total_harps = charlie_harps + carli_harps

    total_instruments = total_flutes + total_horns + total_harps
    result = total_instruments
    return result

print(solution())
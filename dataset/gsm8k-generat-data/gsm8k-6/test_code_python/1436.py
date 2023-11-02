def solution():
    charlie_flutes = 1
    charlie_horns = 2
    charlie_harps = 1
    carli_flutes = 2 * charlie_flutes  # twice as many flutes as Charlie
    carli_horns = charlie_horns / 2  # half as many horns as Charlie
    carli_harps = 0
    total_instruments = charlie_flutes + carli_flutes + charlie_horns + carli_horns + charlie_harps + carli_harps

    result = total_instruments
    return result

print(solution())
def solution():
    
    charlie_flutes = 1
    charlie_horns = 2
    charlie_harps = 1
    carli_flutes = 2 * charlie_flutes
    carli_horns = charlie_horns / 2
    carli_harps = 0
    total_instruments = charlie_flutes + charlie_horns + charlie_harps + carli_flutes + carli_horns + carli_harps
    result = total_instruments
    return result

print(solution())
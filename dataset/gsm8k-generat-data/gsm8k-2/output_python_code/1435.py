def solution():
    """Charlie owns one flute, two horns, and a harp. Carli owns twice as many flutes as Charlie, half as many horns as Charlie, but no harps. What is the combined total number of musical instruments owned by Charlie and Carli?"""
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
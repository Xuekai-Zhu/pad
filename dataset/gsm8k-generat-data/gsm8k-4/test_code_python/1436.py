def solution():
    """Charlie owns one flute, two horns, and a harp. Carli owns twice as many flutes as Charlie, half as many horns as Charlie, but no harps. What is the combined total number of musical instruments owned by Charlie and Carli?"""
    # Define the number of musical instruments owned by Charlie
    charlie_flutes = 1
    charlie_horns = 2
    charlie_harps = 1

    # Calculate the number of musical instruments owned by Carli
    carli_flutes = 2 * charlie_flutes
    carli_horns = charlie_horns / 2
    carli_harps = 0

    # Calculate the combined total number of musical instruments
    total_flutes = charlie_flutes + carli_flutes
    total_horns = charlie_horns + carli_horns
    total_harps = charlie_harps + carli_harps
    total_instruments = total_flutes + total_horns + total_harps

    # Return the result
    result = total_instruments
    return result

print(solution())
def solution():
    """Charlie owns one flute, two horns, and a harp.  Carli owns twice as many flutes as Charlie, half as many horns as Charlie, but no harps.  What is the combined total number of musical instruments owned by Charlie and Carli?"""
    # Define the number of instruments owned by Charlie
    charlie_flutes = 1
    charlie_horns = 2
    charlie_harps = 1

    # Define the number of instruments owned by Carli
    carli_flutes = 2 * charlie_flutes
    carli_horns = charlie_horns / 2
    carli_harps = 0

    # Calculate the total number of instruments owned
    total_instruments = charlie_flutes + charlie_horns + charlie_harps + carli_flutes + carli_horns + carli_harps

    # Display the total number of instruments
    result = total_instruments
    return result

print(solution())
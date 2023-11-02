def solution():
    keaton_ladder = 30  # feet
    reece_ladder = keaton_ladder - 4  # feet
    num_keaton_climbs = 20
    num_reece_climbs = 15

    # Calculate the total length of Keaton's ladder that was climbed in feet
    total_keaton_climb_length = keaton_ladder * num_keaton_climbs

    # Calculate the total length of Reece's ladder that was climbed in feet
    total_reece_climb_length = reece_ladder * num_reece_climbs

    # Convert the total climb length to inches
    total_climb_length_inches = (total_keaton_climb_length + total_reece_climb_length) * 12
    result = total_climb_length_inches
    return result

print(solution())
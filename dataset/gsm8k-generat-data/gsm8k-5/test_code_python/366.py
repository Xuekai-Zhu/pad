def solution():
    keaton_ladder_length = 30  # Keaton climbed a 30 feet ladder
    reece_ladder_length = keaton_ladder_length - 4  # Reece climbed a ladder 4 feet shorter than Keaton's ladder

    keaton_climbs = 20  # Keaton climbed the ladder 20 times
    reece_climbs = 15  # Reece climbed the ladder 15 times

    # Calculate the total length of the ladders climbed in inches
    total_length = (keaton_ladder_length * keaton_climbs + reece_ladder_length * reece_climbs) * 12

    result = total_length
    return result

print(solution())
def solution():
    """Keaton climbed a 30 feet ladder twenty times while working at the construction site. Reece, also working at the same site, climbed a ladder 4 feet shorter than Keaton's ladder 15 times. What's the total length of the ladders that both workers climbed in inches?"""
    # Define the length of Keaton's ladder and the number of times he climbed it
    keaton_ladder = 30
    keaton_climbs = 20

    # Define the length of Reece's ladder and the number of times he climbed it
    reece_ladder = keaton_ladder - 4
    reece_climbs = 15

    # Calculate the total length of ladders climbed by both workers
    total_length = keaton_ladder * keaton_climbs + reece_ladder * reece_climbs

    # Convert the total length to inches
    total_length_inches = total_length * 12

    result = total_length_inches
    return result

print(solution())
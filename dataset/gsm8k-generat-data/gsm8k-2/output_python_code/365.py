def solution():
    """Keaton climbed a 30 feet ladder twenty times while working at the construction site. Reece, also working at the same site, climbed a ladder 4 feet shorter than Keaton's ladder 15 times. What's the total length of the ladders that both workers climbed in inches?"""
    keaton_ladder_length = 30 * 12  # convert feet to inches
    reece_ladder_length = (keaton_ladder_length - 4) * 12
    keaton_climbs = 20
    reece_climbs = 15
    total_length = (keaton_ladder_length * keaton_climbs) + (reece_ladder_length * reece_climbs)
    result = total_length
    return result

print(solution())
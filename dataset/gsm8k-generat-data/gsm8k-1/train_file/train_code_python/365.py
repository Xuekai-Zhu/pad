def solution():
    """Keaton climbed a 30 feet ladder twenty times while working at the construction site. Reece, also working at the same site, climbed a ladder 4 feet shorter than Keaton's ladder 15 times. What's the total length of the ladders that both workers climbed in inches?"""
    keaton_ladder = 30 * 12  # convert to inches
    reece_ladder = (30 - 4) * 12 * 15  # convert to inches and multiply by number of climbs
    total_ladder = keaton_ladder * 20 + reece_ladder
    result = total_ladder
    return result

print(solution())
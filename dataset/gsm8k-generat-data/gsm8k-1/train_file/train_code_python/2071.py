def solution():
    """A box of six popsicles was left out in the sun and is slowly melting. Every time a popsicle melts the remaining popsicles melt twice as fast as the previous one. How many times faster than the first popsicle does the last popsicle’s remains melt?"""
    popsicles = 6
    melt_factor = 2
    remaining_popsicles = popsicles
    total_factor = 1
    while remaining_popsicles > 1:
        total_factor *= melt_factor
        remaining_popsicles -= 1
    result = total_factor
    return result

print(solution())
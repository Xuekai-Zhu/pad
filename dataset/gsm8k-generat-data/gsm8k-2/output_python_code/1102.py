def solution():
    """Martha is making centerpieces for her Thanksgiving dinner. There are six centerpieces, and each centerpiece uses 8 roses, twice as many orchids as roses, and a certain number of lilies. If Martha wants to spend $2700 total, and each flower costs $15, how many lilies will she put in each centerpiece?"""
    roses_per_centerpiece = 8
    orchids_per_centerpiece = 2 * roses_per_centerpiece
    lilies_per_centerpiece = 0
    total_flowers_per_centerpiece = roses_per_centerpiece + orchids_per_centerpiece + lilies_per_centerpiece
    total_cost_per_centerpiece = total_flowers_per_centerpiece * 15
    remaining_cost = 2700 - (total_cost_per_centerpiece * 6)
    lilies_per_centerpiece = remaining_cost / (6 * 15)
    result = lilies_per_centerpiece
    return result

print(solution())
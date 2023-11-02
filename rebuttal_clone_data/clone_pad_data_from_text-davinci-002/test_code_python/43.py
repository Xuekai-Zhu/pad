def solution():
    """An earthquake caused four buildings to collapse. Experts predicted that each following earthquake would have double the number of collapsing buildings as the previous one, since each one would make the foundations less stable. After three more earthquakes, how many buildings had collapsed including those from the first earthquake?"""
    buildings_collapsed = 4
    building_doubling = 2
    total_collapsed = buildings_collapsed * (building_doubling ** 3)
    result = total_collapsed
    return result

print(solution())
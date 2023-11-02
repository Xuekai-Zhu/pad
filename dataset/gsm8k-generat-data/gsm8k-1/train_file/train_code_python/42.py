def solution():
    """An earthquake caused four buildings to collapse. Experts predicted that each following earthquake would have double the number of collapsing buildings as the previous one, since each one would make the foundations less stable. After three more earthquakes, how many buildings had collapsed including those from the first earthquake?"""
    initial_collapse = 4
    total_collapse = initial_collapse + (2**1 * initial_collapse) + (2**2 * initial_collapse) + (2**3 * initial_collapse)
    result = total_collapse
    return result

print(solution())
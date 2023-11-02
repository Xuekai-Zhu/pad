def solution():
    """Tamtam collected 65 shells in total. She got 13 purple shells, 8 pink shells, 18 yellow shells, and 12 blue shells. The remaining shells are color orange. How many orange shells are there?"""
    purple_shells = 13
    pink_shells = 8
    yellow_shells = 18
    blue_shells = 12
    total_colored_shells = purple_shells + pink_shells + yellow_shells + blue_shells
    orange_shells = 65 - total_colored_shells
    result = orange_shells
    return result

print(solution())
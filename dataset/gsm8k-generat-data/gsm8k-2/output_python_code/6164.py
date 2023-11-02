def solution():
    """Tamtam collected 65 shells in total. She got 13 purple shells, 8 pink shells, 18 yellow shells, and 12 blue shells. The remaining shells are color orange. How many orange shells are there?"""
    total_shells = 65
    colored_shells = 13 + 8 + 18 + 12
    orange_shells = total_shells - colored_shells
    result = orange_shells
    return result

print(solution())
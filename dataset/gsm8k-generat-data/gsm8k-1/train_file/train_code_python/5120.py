def solution():
    """Andrea needs 45 rhinestones to finish an art project. She bought a third of what she needed and found a fifth of what she needed in her supplies. How many rhinestones does she still need?"""
    total_needed = 45
    bought = total_needed / 3
    found = total_needed / 5
    still_needed = total_needed - (bought + found)
    result = still_needed
    return result

print(solution())
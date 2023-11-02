def solution():
    """Andrea needs 45 rhinestones to finish an art project. She bought a third of what she needed and found a fifth of what she needed in her supplies. How many rhinestones does she still need?"""
    total_rhinestones = 45
    bought_rhinestones = total_rhinestones / 3
    found_rhinestones = total_rhinestones / 5
    still_need = total_rhinestones - bought_rhinestones - found_rhinestones
    result = still_need
    return result

print(solution())
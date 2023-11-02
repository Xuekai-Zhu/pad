def solution():
    """The Chrysler Building has 11 more floors than the Leeward Center. Together they have a total of 35 floors. How many floors does the Chrysler Building have?"""
    total_floors = 35
    leeward_floors = (total_floors - 11) / 2
    chrysler_floors = leeward_floors + 11
    result = chrysler_floors
    return result

print(solution())
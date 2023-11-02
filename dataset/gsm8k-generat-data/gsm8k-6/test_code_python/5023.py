def solution():
    # Calculate the total number of orcs available
    total_orcs = 10 * 8  # 10 squads of 8 orcs each

    # Calculate the amount of swords each orc should carry
    swords_per_orc = 1200 / total_orcs

    result = swords_per_orc
    return result

print(solution())
def solution():
    """Bugs are thriving in a garden of 30 plants. The bugs are very hungry today and completely ate 20 plants. The next day, they were still full and only ate half of the remaining plants. After that, they ate only 1 of the plants that were left. How many plants remain?"""
    total_plants = 30
    plants_left = total_plants - 20
    plants_left = plants_left / 2
    plants_left = plants_left - 1
    result = plants_left
    return result

print(solution())
def solution():
    """Bugs are thriving in a garden of 30 plants. The bugs are very hungry today and completely ate 20 plants. The next day, they were still full and only ate half of the remaining plants. After that, they ate only 1 of the plants that were left. How many plants remain?"""
    total_plants = 30
    eaten_plants = 20
    remaining_plants = total_plants - eaten_plants
    half_remaining_plants = remaining_plants / 2
    final_plants = half_remaining_plants - 1
    result = final_plants
    return result

print(solution())
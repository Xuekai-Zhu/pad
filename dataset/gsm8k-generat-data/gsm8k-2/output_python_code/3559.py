def solution():
    """Anna wants to grow some lettuce in the garden and would like to grow enough to have at least 12 large salads. She estimates that, despite her best efforts, half of the lettuce will be lost to insects and rabbits. Each lettuce plant is estimated to provide 3 large salads. How many lettuce plants should Anna grow in the garden?"""
    total_large_salads = 12
    lettuce_plants_needed = total_large_salads / 1.5
    lettuce_plants = lettuce_plants_needed / 3
    result = lettuce_plants
    return result

print(solution())
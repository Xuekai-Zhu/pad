def solution():
    """Milo is making a giant loaf of bread, and the recipe calls for pounds of eggs instead of telling him the number. He needs 6 pounds in total. He looks up online that an egg weighs 1/16 of a pound. If he needs 6 pounds of eggs, how many dozen should he buy?"""
    egg_weight = 1/16
    total_weight = 6
    total_eggs = int(total_weight / egg_weight)
    dozen_eggs = total_eggs / 12
    result = dozen_eggs
    return result

print(solution())
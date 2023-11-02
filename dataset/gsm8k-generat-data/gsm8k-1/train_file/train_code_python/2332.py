def solution():
    """Milo is making a giant loaf of bread, and the recipe calls for pounds of eggs instead of telling him the number. He needs 6 pounds in total. He looks up online that an egg weighs 1/16 of a pound. If he needs 6 pounds of eggs, how many dozen should he buy?"""
    pounds_of_eggs = 6
    weight_of_one_egg = 1/16
    number_of_eggs = pounds_of_eggs / weight_of_one_egg
    number_of_dozen = number_of_eggs / 12
    result = number_of_dozen
    return result

print(solution())
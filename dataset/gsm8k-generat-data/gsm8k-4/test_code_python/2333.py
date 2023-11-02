def solution():
    """Milo is making a giant loaf of bread, and the recipe calls for pounds of eggs instead of telling him the number. He needs 6 pounds in total. He looks up online that an egg weighs 1/16 of a pound. If he needs 6 pounds of eggs, how many dozen should he buy?"""
    # Define the total weight of eggs needed in pounds
    total_weight = 6

    # Define the weight of a single egg in pounds
    egg_weight = 1/16

    # Calculate the total number of eggs needed
    total_eggs = total_weight / egg_weight

    # Calculate the number of dozens needed
    dozens = total_eggs / 12

    # Return the result
    result = round(dozens)
    return result

print(solution())